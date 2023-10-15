install:
	poetry install
brain-games:
	poetry run python -m brain_games.scripts.brain_games
brain-even:
	poetry run python -m brain_games.scripts.run_game brain_even
brain-calc:
	poetry run python -m brain_games.scripts.run_game brain_calc
brain-gcd:
	poetry run python -m brain_games.scripts.run_game brain_gcd
brain-progression:
	poetry run python -m brain_games.scripts.run_game brain_progression
brain-prime:
	poetry run python -m brain_games.scripts.run_game brain_prime
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-reinstall:
	python3 -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8 brain_games

