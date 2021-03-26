// Recursive Version

#include <iostream>
#include <cmath>
#include <iomanip>
#include <ctime>

using namespace std;

int cost(string mural, int x, int y)
{
	bool doubt_sign = false;
	for (int i = 0; i < mural.size(); i++)
		if (mural[i] == '?')
		{
			doubt_sign = true;
			break;
		}
	if (doubt_sign != true)
	{
		int price = 0;
		for (int letter = 1; letter < mural.size(); letter++) {
			if (mural[letter - 1] == 'C' && mural[letter] == 'J')
			{
				price += x;
			}
			else if (mural[letter - 1] == 'J' && mural[letter] == 'C')
			{
				price += y;
			}
		}
		return price;
	}
	else
	{
		long long int threshold = pow(10, 7);
		for (int letter = 0; letter < mural.size(); letter++) {
			if (mural[letter] == '?') {
				mural[letter] = 'C';
				int cost_c = cost(mural, x, y);
				if (cost_c < threshold)
					threshold = cost_c;
				mural[letter] = 'J';
				int cost_j = cost(mural, x, y);
				if (cost_j < threshold)
					threshold = cost_j;
				mural[letter] = '?';
			}

		}
		return threshold;
	}

}

int solve()
{
	int x, y;
	string mural;
	cin >> x >> y >> mural;
	return cost(mural, x, y);
	
}

int main()
{

	int t, i = 1;
	int solution;
	cin >> t;
	while (t--)
	{
		solution = solve();
		cout << "Case #" << i << ": " << solution << endl;
		i++;
	}
}

// Iterative Version

#include <iostream>
#include <cmath>
#include <iomanip>
#include <ctime>

using namespace std;

bool is_doubt(string mural)
{
	bool doubt_sign = false;
	for (int i = 0; i < mural.size(); i++)
		if (mural[i] == '?')
		{
			doubt_sign = true;
			break;
		}
	return doubt_sign;
}

int cost(string mural, int x, int y)
{
	bool doubt = is_doubt(mural);
	while (doubt)
	{
		for (int letter = 0; letter < mural.size(); letter++) {
			if (letter == 0) {
				if (mural[letter] == '?') {
					if (mural[letter + 1] == 'C')
						mural[letter] = 'C';
					if (mural[letter + 1] == 'J')
						mural[letter] = 'J';
				}
			}

			else if (letter == mural.size()-1) {
				if (mural[letter] == '?') {
					if (mural[letter - 1] == 'C')
						mural[letter] = 'C';
					if (mural[letter - 1] == 'J')
						mural[letter] = 'J';
				}


			}

			else if (mural[letter] == '?') {
				if (mural[letter - 1] == 'C' && mural[letter + 1] == 'J')
					mural[letter] = 'C';
				else if (mural[letter - 1] == 'J' && mural[letter + 1] == 'C')
					mural[letter] = 'J';
				else if (mural[letter - 1] == 'C' && mural[letter + 1] == 'C')
					mural[letter] = 'C';
				else if (mural[letter - 1] == 'C' && mural[letter + 1] == 'C')
					mural[letter] = 'C';
				else if (mural[letter - 1] == 'J' && mural[letter + 1] == 'J')
					mural[letter] = 'J';
				else if (mural[letter - 1] == 'J' || mural[letter + 1] == 'J')
					mural[letter] = 'J';
				else if (mural[letter - 1] == 'C' || mural[letter + 1] == 'C')
					mural[letter] = 'C';
			}

		}

		doubt = is_doubt(mural);
	}

	int price = 0;
	for (int letter = 1; letter < mural.size(); letter++) {
		if (mural[letter - 1] == 'C' && mural[letter] == 'J')
		{
			price += x;
		}
		else if (mural[letter - 1] == 'J' && mural[letter] == 'C')
		{
			price += y;
		}
	}

	return price;

}

int solve()

{
	int x, y;
	string mural;
	cin >> x >> y >> mural;
	return cost(mural, x, y);
	
}

int main()
{

	int t, i = 1;
	int solution;
	cin >> t;
	while (t--)
	{
		solution = solve();
		cout << "Case #" << i << ": " << solution << endl;
		i++;
	}
}
