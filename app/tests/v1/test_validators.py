import unittest
from app import create_app
from app.api.v1.utils.validator import TestValidator


class ValidatorTestSys(unittest.TestCase):
	def setUp(self):
		self.validt = TestValidator()

# question specific
		self.missing_meetup = {}
		self.meetup_present = {"meetup":1}
		self.all_present = {
		"meetup": 1,
		"title": "The blue shorts rock",
		"body": "The other day I was literally supposed to read all about the adventures of some crazy fella in mara",
		"votes": 21
		}
		self.all_present_wrong_instace = {
		"meetup": "The dark haired girl",
		"title": 12,
		"body": 34,
		"votes": "The other day I was literally supposed to read all about the adventures of some crazy fella in mara"
		}

		self.maxedout_data = {
		"meetup": 2,
		"title": "yXXrmiA6bFO1Xz7IvdllCf3Fucsyp7LA3vTOVMiyEiJuUEfthOwerwe",
		"body": "AuFONQw2Xq48H7RLtIC0lmm6ltsrkkMALQ0m4pok7ef2LkrwpSCTuJd5H34wn82L8VBbfloL4Z9wZLRPXB75SVIzlKYlFLhbYtmqfwpXsRDe0ZZMmuPsCat432jCAxJ5S0BRyn79N9Ut5XMAaW3j9PvDOY590a6zmm7NNXUgfMlrxw62N29yAxICmFfZCBPlAVYkoL3cFDzKhXpBCsRB4SF1EG8YAz2lepfLaRSNXnrqr0T9Y4kIOimEtUOvHi9DJBkrlLHXs6AMzO9ObopmyKI2R7iv7jpWwp5RvEufsYF2ncpNdvucO6QSQ5ItErg62ytbHDaSQueQrtyE1wYPYB1Cv86ohv7L6ssUMQKZWlD7cmPJtKHS49NX78XLdgo561cG3GNmvD3IZv4BTfKt6nV2S3DEJ5den6GMDEYcnXUIRydfeE5pGnmhy6ppbh7X2FZ9mCTRJKHHx0wQ1HQvSdpBzOuAJuts75ItYEGgjI5srMHAm9iUtpJI5VK9bd6oHaMIiwQ7BlCtwwQ5KiydGZLvhehnILrdNzE2lca1jqQP0PQib0cXRtNvvlzA2uLPBbtlLDS3DHKc0ixWbuPCBSCJt2KL8fAr34SaveA4IYywgkIMXLadkJ92BRsVsQnSS4iI1Hq69jw4AcKslJqVMjIm2cPBFTqIdybPAdkB5idsj6We4ixl8Ke5CFCbSKTjDSOADhyWFQN5NzReZWZ20vApcWVEV3Os7UxzVPcSbfIuQIWO82IYJCv5ZhkQ1jNEKVh4PnWJzRQZaX78J9Yzs5Ryeh0hvgvEbfmXvKbq95muLwk3nYxu5ntStXdJoiU7pdEvOXBn4LFQnJedtDLL1KMi5TifOuGI3LS15NuKEXaKfrcxxaqJlNz2tUzuHohlOctniXxWigL7vowVqa5Nb6yYHoQZMMZswhR6sFAilThKWkxZw9OWjpAfd8eeH8eybTZeQ19c0wHcwzTVGH5tLUkdufh75z8PVXkxMHgAqjiCTGVmyfqSxgOVxg8yrFvUsOA5LMOqDeetMTrsqsUnVF3N1noERYx1v4JnjEpabcyMGcYEeDomjDucRkdkH6v1YWmna6w86axXRPJrYffQlCenN9uL1XaVF7PLNJtj62aO0rWiPUBLO9t9VovBQCZuF9vMOVnc8D4cT6mZDAxroiH02ggCyzB7VyXUAvCjnK6pXrNqbjLYiut04RlhhqCMbFuFjNnd3GfWJmjGzO0bTcL8GpEKt3lajftFoHgB0VsEvSWSYM36879zo5ZhkCy612lfMo3caFrNpJwMmxeRp3R0CEl2yLkrFjMcHOHFYL8Ed4OaTzvIojqjyYP19BsLxPNhtqSRNwooJt2R7irn3txGyaZFs6RPzsFC6GxstiQtBvjmOFi5az8g2sagbYmvelh7hTj8MlKExYKFIdtX4KZLw6BuPmJTIhczEXvNTdYlgJ9SvQmIG28smkoHcHvkPYfYAR3mP0XFb1f2IHfjkWi5HhuVdfsdfs",
		"votes": 12
		}
		self.minnedout_data = {
				"meetup": 2,
				"title": "lu9he8inLPr1MF6qlt",
				"body": "1Z4G70z8cLp4gYqZpEUY29EKoW5zLKHDczA5dO6aO0dmjnwoW5hOdTXc3Va30Od0RvFSpwCAN44oyfx77UkZ4FLsymaPmw3OvvofG1TnIOaFwVKCgFrbKbRlyvaN4AQLKJTMbQQduS5qqilV4snXSbp3IaoZmEIAtZoH0TvD1KhJaJ0p41eFMbsvGksgW0GoUiCj92ho6eMTei6RmmSV62xnVBJyuDGj1jsuCFN934otNHXlYBkCH004PAK7DhSZ5hw0W7ksnfmEWKRyuCS2cMMUJQhagdlqOkVDG1T6b6gUuyqYpEcidMDC5LokGYIAyaLkRjC98IxAkqCfGBPkrNuVh9TosCEq55t0Zv71wMcixp3lZS0ddFkuRCRlcyEjrz2eHB0jyaHRzTY01oVR8Neg3UI77JLQJyNzgj6v2XrhdxhPqSAQjiecdRagWdJcruQSw8eJS53HqWgl8yUksocsu6j8oLblL7Ep3d5rnVphQGO9V",
				"votes": 12
				}

		self.nothing_provided = {}

		self.meetup_provided ={
			"location": "kangundo",
			"topic": "how the world ended",
			"happeningOn": "12-43-2017",
			"tags": ["water","war","corruption"],
			"images": ["data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUSExMVFhUXFxUVGBgVFRUXFRUVFRUXFhUXFRcYHSggGBolHRUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGBAQGi0lHR0rLS0tLSstLSstLS0tLS0tLSstLSstLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBIgACEQEDEQH/xAAcAAACAwEBAQEAAAAAAAAAAAADBAECBQAGBwj/xAA9EAABBAECAwYEAwYGAQUAAAABAAIDESEEMRJBUQUGImFxgRORofAysdEHFCNCUsFicqKy4fGCFUNTY3P/xAAZAQADAQEBAAAAAAAAAAAAAAAAAQIDBAX/xAAhEQEBAAMAAgIDAQEAAAAAAAAAAQIRIQMxEkETUWEiBP/aAAwDAQACEQMRAD8A9lAysLR0z0pHAaGUxpIC275rjy1XPD7EQtVIwjt2WNawo+JQ1qbkZYQ2MVSlp0TFd8auAFNIPShagkI1ruBMKtVo4sojY0xHGlTkV+DeUIxJwtoJVstnbCmbXQpYsJN+lWg8Wl9Syhuqgef7W03QLElYvQzWVmaiLK6ceTTK96yCxUfEtExpeaEqtqjHnfus2ZpK3J9KszUts0rhsediGQm9RHSTfa0MeHIVZtl0GoACrqZwQgEyADhJ9py8WyJNNjCzdXLhAZ2ocgEq0zrKoEwG9WY4qHhc0oAsiEHLnFUSDnFSFxVQgLKLXWpQH6whaihDYixNXnVlB2MRQxWhRXstRtpIGEPhymWMQJcGk4KhxoKjXWrTNrKiNiqRKwYitiRIWIqW1SBhqIxSGqxakrSkjVUNRHhVKDVLUrquivJqmpKWa9gqxxqblCGpaFnTNT+oWfM5byMy0gFqjgiOC7gVLhDUR2FiajT2SvSSNpYs7clVibEmiPNZ0hq1vamIkLF1unx95WsDPfIgzOtEmFJN4NqiAmNLO1Eh2KelaVn6wbIMoqEqXBVcgItWaqkLmlAEcEMqXFDQFyENyta6kgqArALguJQH61pEiVWNrnuixsXmszUaPaA1GaFK4pqBQJWVJMbz9hamrfhZU5BNLXxxGZqTUhzQLTenorHaEeKQjKu4fpMy71sxhEKW/euWNkF+tNkLL42tvlI0LwgOmo74Sh1nVBD7KqYJuf6aBks+X6pXVagHAUg0L80s5OYlbVCUDVzcDHPr8LS71oWmCl5hYIVlpl67XEcVt2BPMXiQjli/hjG/i8kprJi0G27Bx9SA40ausN+vsnpYXHctPXB5VXP1Sz4D1b8irhlJZzxcNC/etnkWdv5fr5KrdTsawSPa8Z9zXzPJHMDvL7v+5HyVHQOrcbHr+qaiOq1Lv9wx5EDPln6LKmuzfXhJ5War53Xrhbbonb2PPf3QXt8h57/qnKbGmdw45LI7QkB2W/q4RyysXU6Qk1S0xDz8xVI2lbEug6oMunoWSABzKvZMWRpNhZGvsHhPTC9XLpfcLI7bgttDFZ9Uw84XKWhdFGXGk4dLwpglwLiAmHRpeQZSCjiq2uKikBNrlYNUgJANcruCpSA/VEWus7YWvppmnY4+915yAp2IHkfNceWEY45PQMcEVzsLN0T73T0hNLC46rWXgU58JB35LKCflf4bo+VpFoW+E0zyXaERrbVY2WmY2ULCq0pAaVneSK9lev5KlIgsUa1GYFRoV0U5FyQUMhcFYNUNAyEGZMkIbmIPTPc1BdGtJ8aE9vkq2NMuRiG5ifljSz22ns2bIaQgywnNRGOiWJVGAWjakjqmgWQnJnLN1IKuEz9UByWF2rqW/DeNqFnf1/stTtSURgEn8Ww8hufYH7teTn7RbI2bBHhoA+bXEfk77K0kDQGsADzyFnpg2f1SfaE7ctJzRpZ+rl8Nczw9bFg7Vv8AXmseXUOc7iJyVUgPaI+P/wAT+USdeCVmxvogtIsg3e12PLo0LRfNXD52fq0f3QLC0kCV1ENLS1DuaVfNaCZzo6VBhNTUUsUBAKkqFFpBBUhQVKA/ScT82tPSv6+1rJaOSf0xHO7+i58o5o3tMKrCM2akCKQUPb6/e65pz5FczeByz8R6KYtNYx7I0MIsk1+nS/NeQ7Z/aTptPO6FsbpeGg57Hs4QSASG1fERdG6yCOS0m7zEvj+3rXQVtugP7QjZfHIxoaaPE9oAJyAbODuV8x7R/aNq3ud8ENjY4AAOZxOBbdkOBqzjBGK5rzEemJbbg8vBvieS0jG5I/EM1QV/HU6cxfcf/U4LIM8VjcGRlit7yun7TgYPFNEM1mRgzv1Xxxugi3+ILxdDnuKN4Hqp1ErcAEm8Yb+Z2wpl36O4Prg7c03/AM7D53Y+eyDq+8enjAPHx3sI/ET/AGHuV8nMxw28dQCRhamk0gI4sDFk0bHoL3+8KtU5jHs3d94RX8KWjueFuBkAgA5yNt6zsmI+90JoiOc2axGDXUmnbCvXyXiZmxs/GSXb3nYUD9Tvn9a6XvLwEMBGPevl7fZT1NNZ4rX1JuviIvix/ld+iNGQ4cTSCOoyF8xf3odyDjtyPJGHeCg54eWOIAsEg9ao7n1WNum2H/Lcn0ctQnNXhewv2gniDNTwEcQbxN8LxZric001zaIJLcjoveMma/LSHDqPvC0uNx9ualHsQHsWm5gSuoYaKUoYWqGaSr2JzUHNlUZDeVpAQdDaT7RprCTsASfQblbRi3Xzbv33hAbJFHZFOjc/kSfC5rfmc/pm8ZsM7tfVnVNb8MhnDxGnOpzr4S3OzdupteUkje3BFbA11zW2/rshQ69wxy89/mnNLrG8Qz5UTyu69F0a0NRWTSzGvARXlzriz7JdmjfV8JAPtfT12XoYNY0MLA7wmz4sltCqaato9+mMIUuqFcTrIrhAvOC31HIlSfv2wZY3DfiB2o2PvdMyyh3ALqm7uB3ryB6Barntq6HEc1Y4KyAQORNHGNhvuk3hvAbjBLhhx4hwkE3wgOo2K/EOSVvOCTvQ5nE++Uo61Usc0jB5HFj5oheMZHzTTQCq0mCBuguGUErSksXPeFxkCQDcuChy4OQH6PEnkjRzgAuscIFk2KAA3vovkTNY9jDEJXhp4hwh2MjxB1nnRPL6lUDHBvDxODSN2muLFUQeVrC5RjPG+tRd69OGOcJm00Emr4jXJoI8R5UOoWXqf2nMDCGQPLjsSWnhOKLgDkeXkvn+mDCeEkuHMWMOGMc8nHXKHPIGylgAAApxNmz0APLzo3ajlvppMdCdr9s6jUSOfLI83gND3BrbA8LG3tgY8ue6Rh0Dicged7eyJ+9Hiqmtr8PntzybT0LyXeLGLFivbz3Wnyyk4qQGGXgfwtZxbEkk7f4en/B6Jn4j3HhGBZvck36/kjs0t5o3jfduaxfPZNcFGzV1k8zfPCnm91cxtdFpxgGz5HHLcUjs0RIrN1eff5oDe0xxh3CDQIPDsMdKu8BORa5jqcH1zGd8ZA5f9I9K+FNdmaBnGeLJsAZ8ske9rS1fZ0h8UFOH8zMB2xw07H3pKQdpx0L4SWnl9+q1dP2kGjZw52WkV71hRlltUxuL592n2fNxF07ZGb4LXBoHlyI80FmhrxM/7X1BnbgNeKx9EUaHTz2HNYDQs1TvYiij8jaZa9x43Q935ZdMdTA8y8Di2SEx8MrCACeGnOEmHNOKJB2vwonZna/7tTyBJE6mvjcA4Pad64sAgZ+hwV6rumRptbLpg62SNBaf8bGB9epY51//AJhR+0PugJ4nTadn8VtucxuPijd3COUnPFcWbybS3uw8fJjLZn2fRSfuBoNY1s+nlljY7NROaWbniBbI0lpBsVeOi9X2H2NFpIWwxA8IyS6i5zqoucQACcAYA2C+Z/sw7x/Cl+A5xdHMWhuMRyAUR1zYBHkNqN/XSFfl+U/zbxxgyFDdlHIS8pAWcN4f9p8+o0+kGo0z+BzJG8fha4Fj7blrgQfEWfVV7i95xroS8tDZIyGyNG1kWHNvIaaODtRGd1v96OzP3vSTacEAvZQJNDjBDm2awLAtfDO7HeCXsvUSMkiNk8ErCQHeHajkYsnG4O+bXThJlh/YmvpHfnvJ+78MTb+JKHGx/Ixoy4f4icD3PIX8c7QcSNjWBtj2++S+q99W6LWaZr3TNimAa+EuOT8VjZGse0Wac1zDW7bvyPzYaZ5bRAHI7eEflnPP81p4+Q2Gjs0rjy91qN0bWua6hg8udD032+qvPO0cr6X/AHWlyExZ0WmcMlwA/wCFafVCuEAbVec53/IKNVqDdFJEpa30t2cMDU42TcE4fQJJoUBy9P8AlJN0Uh/9t5/8XfohuaWmiCD0OCjQlbgjdxAcxf8AZJ6zR8PiFU4cQFg48/8ApTo9WCfETf0wjtAc8E0Wt2F2K33+qUh2s4PVHFPamFpF8ztnYJBza3SJRyhX4VVwSJ1qUO1a0BvVwn8VZ6mweuN91qaPUOPCBRGb5DG30/LdYrOEm3DbGDV+p6LZ02kEgwSwYoDc16kY9Vh5Na6BH6sOOxDv8wGKNUPms3tBhJDm3n3NjzsrcOiDW3xG+uBmsgcz7dFXTxudTfDjoPl719lLC67Bon2NFIDxPBqv5qrN+4W9pYAXCwbsc8ZOwv7Cbbo2tDceI8+QH52rOeGi8CqP03VXNeOCJI+EWC0ZHyvkOS9d3e7rNoS6loc45EZ/C0H+sfzHyOB0vandbsDI1E48W8bCPw9HvH9XQcuedvXNCz2Wef1FJuzIXlrnQxOLQA0mNhIA2AJGAn44gQBQocqwPZCa+keORTWexGNDdgB6CkQOQ+NSHKVE9b2TBLfxImknHEBTxfR4yPmvnPdbs6R+rOn1D3FrRK00Q0ufG4AZAuq4ivqYKV/cIfi/G+Gz4v8AXwji24d+tY9MJ7aYeS4yx860EL4tYAXFzmaoM4nficx0vBZ9WO+q+nWvMdsd2XSagTxyiOyxzgWl3iZVFuf8LceXmvRSPR7X5LLqwqzsuASmcQxCU7yBjRIcUbdV7YRpZaUPelZHIZCfvHVKyT2h6h6VLgqkAxkyvCftP7ts1MX7w0cMsQtzqvjiG4Pm3cHpft7RqF2pAHQSt/qje32LSD+avG6ofAp9FrnkSv0+odbRTvgvog26weGjZcT7peSaZgose3Nm2EZFb2F+heyz/Bi6/DZ/tC582/ktfy/wfT83HXOO5JVHylxAAyegyT0X2rvD2ZBqPDKwEciMOB8iMrAi7F08F/DbR/qJ4nV6nb2WkzhPD6Tu+85lPAOm7j/YL0GjiiiHgYB57uPq7dFmNk9ElMj2Rh+t3CztZAJRTvY8x6I7W2plACYeV1WmdG6j7HkVaDUkfeFvTkHByF5/V6fhOMt5f8p+zOmUYwL3RJohV/8Aeyy2SkIzdQSp0e0SQ1t5oDk06S6QpGpDWy6lSQuAQltxM8QFWTtWb8gtXSOkDgc0eVNz89lztMIiQT4tjewvb++FRkjiMEAfLnz6qLNiH5IyXkF93XCL5E7H6J6BnCMuyeQG4N8/fZK6SK6OMG7oXbdvbKI0lzmsaC55NBoGXGj9+QyVHrkaY4j6jVutoAsmgABkknAAHPkvbd2O7nCRNOAXjLY8FsZ5F3Jzx8h5nI7u33dbD/Ekp0xHL8MfUM8/8XsPP00RU1nn5PqGWNRAENjkZpUs0tciNehELmpGaBVg5BBVrSMZpVkEPCIHKaqIehFEcUFzkGpI6ko+RGmKzNW48lUCNRKkp5qQnPIKW1DlpIDUGsoqJ9aSCOVEfRZ3GqvJvdVoNfs+UfBjIP8AIwf6QkNbruEFZ0eu4WMF/wAjfyWT2rrb2KcxCdX2kLOaWZqtYDzWXqZjlJTTLWQG9ROAgunBSD5SUIOVE2GUcoM7gUm1xrdQJaQFnBIzAc0zJOkZnklAKTRVtshtKYeUu4INcPVw7CXRRIa4eV3yu9t0qIJJdXy5e3ly3+q6aItcWncdCCNr3CGAp9Akq9ev1NPeXYFk3wt4RdbgcslTsAOhsX578lWbUtFn6EBavYnd2bVU51xQ78VeJ4/+tp/3HHqst2nZMZ0p2a2WaT4cTOJ/+lrduJx2AH3ZX0nu32AzTNu+OUjxPIr1awfyt/Os+RuyezooGfDiaGjc/wBTj1ceZWm1Tawz8ly59CNpEjcg0iNClmYRGOpBaVcOSMxaglC41YOSUIx6JxJVz6XfGQYzn9Fds6UaQpc5JUOl6DJIl3TJaSZKQzL3eaTlCkSIeonwqhsyd2SlHvJRNU7mEhJqQAtZCFmnAwlHzfmlJ5c2hST4V6Ac0h4W/wCUD6BZWvnKa+MeAHyH5LI1M+VUABfikhO7KYc6klI+ymEcJR2wYtRCjhMBmLCWnam3zAYSGpnQA3OSsiI99oDymHFVIVSVUlIKOChXVSEwkOXWqrkjfZOxO6cUZD5f4sgyOIfw2nybzPmfal6uMpRrkwwrCua5W3dMMcjNclmORQ9SB2yIrZLSjXqWvQGgwomEkyVH+JhTVQXi81UyhLfGQvio0ZwyqjnpN83zURyp6UebMqun80nK/CAZktGddNXNAM1lJSahd8YKtG0XSCt0lJL0Skmq81UakFOQ1NY+gSsZ0q0ddLxBZZDQtMSBkd0SGpmKNqZRyWZqJ8KwpqdWeqTkktAnmyqGQUmYWol5JRzkScpJz0A7HKi/HWaJVb4qAO+W0vI5QHqrigOJQ3K5chkoChUKxVUglQuXJhBUKy5Aff2ogcuXLBzCsci8ShclQIw+as5y5ckqOBpXEy5chUgUk2VHxxsoXIMMv6qGSealchSzpeqz59QuXJ4kC7UBCklPJcuV6BUzElRI4rlyZgyOIWfLqwMLlyuBnajULO1E1rlyambM5UjepXIAEj0q9cuQA1IXLkwlQVy5AVKqQpXJBVQuXJBy5cuQHKFK5Af/2Q==",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRpz_abZdvmNm2Y3XFLgRPwlDXUxiL6LIaOgQcYpIg1MYtGxUf",
			"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR0LtXGROaByFTm9Q4FyaUVbSmAb5oZNdZwQcHboId0rwrblz2S"]
		}

		self.max_meetup = {
			"location": "pvmtcxt6gqaRYlmsWW2gTDmAZvEthT74WV4x2GtXKQvmQXyES6dvXTLDHms3OclAPToSyq5ryMQBkQz9viN2SEUx4nQT99xSBhNgtf",
			"topic": "gAhzgsoXLyz6WEuEQ02EkuZGxChLvzwRD1xZT1Q3JZtSEE0ZoaCupFw4D3UV7CwnbOPoKfFtyGBV0nIEuMB37pWG8SAF3zFhfvjEtyr",
			"happeningOn":'b8dwst4IfDllvtV3O0vogVNw0r34',
			"tags": ['girl','boy','shoes','comps','goats','music','we','fly','extremes','funny'],
			"images": ['imageone','imagetwo','imagethree']
		}

		self.min_meetup = {
			"location": "xe",
			"topic": "er",
			"happeningOn": "rW1v90"
		}


		self.meetup_wrong_type = {
			"location": 12,
			"topic": 12,
			"happeningOn": 10,
			"tags": "corruption",
			"images": "banana"
		}

		self.rsvempty = {}

		self.rsvnorm = {
		"meetup": 1,
		"response": "yes"
		}
		self.rsvodd = {
		"meetup": "yes",
		"response": 23
		}

# question specific

# question specific

	def test_empty(self):
		resp = self.validt.emptyrequest('something')
		self.assertEqual(resp, False)
		resp = self.validt.emptyrequest('')
		self.assertEqual(resp, True)
		resp = self.validt.emptyrequest(None)
		self.assertEqual(resp, True)

	def test_meetup_present(self):
		resp = self.validt.meetup_id_provided(self.missing_meetup)
		self.assertEqual(resp, False)
		resp = self.validt.meetup_id_provided(self.meetup_present)
		self.assertEqual(resp, True)

	def test_title_present(self):
		resp = self.validt.title_provided(self.meetup_present)
		self.assertEqual(resp, False)
		resp = self.validt.title_provided(self.all_present)
		self.assertEqual(resp, True)

	def test_body_present(self):
		resp = self.validt.body_provided(self.meetup_present)
		self.assertEqual(resp, False)
		resp = self.validt.body_provided(self.all_present)
		self.assertEqual(resp, True)

	def test_votes_present(self):
		resp = self.validt.votes_provided(self.meetup_present)
		self.assertEqual(resp, False)
		resp = self.validt.votes_provided(self.all_present)
		self.assertEqual(resp, True)

	def test_meetup_is_instance_of_int(self):
		resp = self.validt.meetup_instance_of_int(self.meetup_present['meetup'])
		self.assertEqual(resp, True)
		resp = self.validt.meetup_instance_of_int(self.all_present_wrong_instace['meetup'])
		self.assertEqual(resp, False)

	def test_title_is_instance_of_int(self):
		resp = self.validt.title_instance_of_str(self.all_present['title'])
		self.assertEqual(resp, True)
		resp = self.validt.title_instance_of_str(self.all_present_wrong_instace['title'])
		self.assertEqual(resp, False)

	def test_body_is_instance_of_int(self):
		resp = self.validt.body_instance_of_str(self.all_present['body'])
		self.assertEqual(resp, True)
		resp = self.validt.body_instance_of_str(self.all_present_wrong_instace['body'])
		self.assertEqual(resp, False)

	def test_votes_is_instance_of_int(self):
		resp = self.validt.votes_instance_of_str(self.all_present['votes'])
		self.assertEqual(resp, True)
		resp = self.validt.votes_instance_of_str(self.all_present_wrong_instace['votes'])
		self.assertEqual(resp, False)

	def test_title_max_length(self):
		resp = self.validt.title_max_length_reached(self.maxedout_data['title'])
		self.assertEqual(resp, True)
		resp = self.validt.title_max_length_reached(self.minnedout_data['title'])
		self.assertEqual(resp, False)

	def test_body_max_length(self):
		resp = self.validt.body_max_length_reached(self.maxedout_data['body'])
		self.assertEqual(resp, True)
		resp = self.validt.body_max_length_reached(self.minnedout_data['body'])
		self.assertEqual(resp, False)

	def test_title_min_length(self):
		resp = self.validt.title_min_length_reached(self.minnedout_data['title'])
		self.assertEqual(resp, True)
		resp = self.validt.title_min_length_reached(self.maxedout_data['title'])
		self.assertEqual(resp, False)

	def test_body_min_length(self):
		resp = self.validt.body_min_length_reached(self.minnedout_data['body'])
		self.assertEqual(resp, True)
		resp = self.validt.body_min_length_reached(self.maxedout_data['body'])
		self.assertEqual(resp, False)



# question specific
# meetup specific
	def test_location_present(self):
		resp = self.validt.location_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.location_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)

	def test_topic_present(self):
		resp = self.validt.topic_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.topic_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)

	def test_happingOn_present(self):
		resp = self.validt.happeningOn_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.happeningOn_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)

	def test_tags_present(self):
		resp = self.validt.tags_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.tags_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)

	def test_images_present(self):
		resp = self.validt.images_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.images_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)

	def location_is_instace_str(self):
		resp = self.validt.images_provided_meetup(self.meetup_provided)
		self.assertEqual(resp, True)
		resp = self.validt.images_provided_meetup(self.missing_meetup)
		self.assertEqual(resp, False)


	def test_images_is_instance_list(self):
		resp = self.validt.images_is_list(self.meetup_provided['images'])
		self.assertEqual(resp, True)
		resp = self.validt.images_is_list(self.meetup_wrong_type['images'])
		self.assertEqual(resp, False)

	def test_topic_is_instance_str(self):
		resp = self.validt.topic_is_str(self.meetup_provided['topic'])
		self.assertEqual(resp, True)
		resp = self.validt.topic_is_str(self.meetup_wrong_type['topic'])
		self.assertEqual(resp, False)

	def test_happeningOn_is_instance_str(self):
		resp = self.validt.happeningOn_is_str(self.meetup_provided['happeningOn'])
		self.assertEqual(resp, True)
		resp = self.validt.happeningOn_is_str(self.meetup_wrong_type['happeningOn'])
		self.assertEqual(resp, False)

	def test_tags_is_instance_str(self):
		resp = self.validt.tags_is_list(self.meetup_provided['tags'])
		self.assertEqual(resp, True)
		resp = self.validt.tags_is_list(self.meetup_wrong_type['tags'])
		self.assertEqual(resp, False)

	def test_location_min_length_meetup(self):
		resp = self.validt.meetup_location_min_length_reached(self.min_meetup['location'])
		self.assertEqual(resp, True)
		resp = self.validt.meetup_location_min_length_reached(self.max_meetup['location'])
		self.assertEqual(resp, False)

	def test_location_max_length_meetup(self):
		resp = self.validt.meetup_location_max_length_reached(self.max_meetup['location'])
		self.assertEqual(resp, True)
		resp = self.validt.meetup_location_max_length_reached(self.min_meetup['location'])
		self.assertEqual(resp, False)


	def test_images_max_length_meetup(self):
		# images list test whether larger than allowed number
		resp = self.validt.meetup_images_max_length_reached(self.max_meetup['images'])
		self.assertTrue(resp)

	def test_topics_min_length_meetup(self):
		resp = self.validt.meetup_topics_min_length_reached(self.min_meetup['topic'])
		self.assertTrue(resp)
		resp = self.validt.meetup_topics_min_length_reached(self.max_meetup['topic'])
		self.assertFalse(resp)

	def test_topics_max_length_meetup(self):
		resp = self.validt.meetup_topics_max_length_reached(self.max_meetup['topic'])
		self.assertTrue(resp)
		resp = self.validt.meetup_topics_max_length_reached(self.min_meetup['topic'])
		self.assertFalse(resp)


	def test_happeningOn_min_length_meetup(self):
		resp = self.validt.meetup_happeningOn_min_length_reached(self.min_meetup['happeningOn'])
		self.assertTrue(resp)
		resp = self.validt.meetup_happeningOn_min_length_reached(self.max_meetup['happeningOn'])
		self.assertFalse(resp)

	def test_happeningOn_max_length_meetup(self):
		resp = self.validt.meetup_happeningOn_max_length_reached(self.max_meetup['happeningOn'])
		self.assertTrue(resp)
		resp = self.validt.meetup_happeningOn_max_length_reached(self.min_meetup['happeningOn'])
		self.assertFalse(resp)

	def test_tags_max_length_meetup(self):
		resp = self.validt.meetup_tags_max_length_reached(self.max_meetup['tags'])
		self.assertTrue(resp)
		resp = self.validt.meetup_tags_max_length_reached(self.meetup_provided['tags'])
		self.assertFalse(resp)

	

#rsv specific

	def test_rsv_meetup_present(self):
		resp = self.validt.rsv_meetup_provided(self.rsvnorm)
		self.assertEqual(resp, True)
		resp = self.validt.rsv_meetup_provided(self.rsvempty)
		self.assertEqual(resp, False)

	def test_rsv_response_present(self):
		resp = self.validt.rsv_response_provided(self.rsvnorm)
		self.assertEqual(resp, True)
		resp = self.validt.rsv_response_provided(self.rsvempty)
		self.assertEqual(resp, False)


	def test_rsv_response_instance(self):
		resp = self.validt.rsv_response_is_str(self.rsvnorm['response'])
		self.assertEqual(resp, True)
		resp = self.validt.rsv_response_is_str(self.rsvodd['response'])
		self.assertEqual(resp, False)

	def test_rsv_meetup_instance(self):
		resp = self.validt.rsv_meetup_is_int(self.rsvnorm['meetup'])
		self.assertEqual(resp, True)
		resp = self.validt.rsv_meetup_is_int(self.rsvodd['meetup'])
		self.assertEqual(resp, False)



#rsv specific

# other specific

	def test_response_correct(self):
		resp = self.validt.rsvp_response_correct('yes')
		self.assertTrue(resp)
		resp = self.validt.rsvp_response_correct('no')
		self.assertTrue(resp)
		resp = self.validt.rsvp_response_correct('maybe')
		self.assertTrue(resp)
		resp = self.validt.rsvp_response_correct('yeo')
		self.assertFalse(resp)


# other specific

# meetup specific


	def tearDown(self):
		self.validt = None

#present
#instance of int
#max length/min length
#spaces

#post user
#firstname(string), lastname(string), othername(string), email(string), phonenumber(string), username(string), isAdmin(boolean)

#function to analyse an entire request and go through all the required tests
#also test for spaces...links....emails

