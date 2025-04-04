#Python: Core Language Assessment - Basic Language Features - challenge_1.py 3/3/2025
def the_good_bad_and_sorted(sequence):
    '''
        Args:
            sequence    | An iterable consisting of str objects.
                        |> Convert all strings possible into int objects.
                        |> Any string that cannot be converted into an int will remain a string.
                        |> Example: ['N/A', '21', '42', 'MISSING']

        Returns:
            A (2)tuple of lists consisting of good and bad data. (good: list, bad: list)


        Implement this function such that it returns a tuple containing good and bad data.

        Good Data:
            All strings representing numbers must be converted into int objects.
            All even numbers returned in descending order.
            All odd numbers are removed.

            Examples:

            >>> sequence = '100 85 37 50 N/A 66'.split()
            >>> the_good_bad_and_sorted(sequence)[0]
            [100, 66, 50]

            >>> sequence = '1 2 1 4 N/A 1'.split()
            >>> the_good_bad_and_sorted(sequence)[0]
            [4, 2]

        Bad Data:

            Examples:

            Any string which doesn't convert into an int is considered bad data.
            Bad data must be sorted alphabetically in ascending order.

            >>> sequence = '1 2 1 4 N/A MISSING 1'.split()
            >>> the_good_bad_and_sorted(sequence)[1]
            ['MISSING', 'N/A']

        Results:
            Once complete this function returns a tuple containing two lists objects.
            The first list contains good data.
            The second list contains bad data.

            >>> sequence = '2 3 4 5 MISSING 42'.split()
            >>> the_good_bad_and_sorted(sequence)
            ([42, 4, 2], ['MISSING'])
    '''
    good=[]
    bad=[]
    result=()
    #sp = sequence.split()
    #print(sp)
    for i in sequence:
        #x = int(i)
        try:
            x = int(i)
        except:
            #print(Exception)
            bad.append(i)
            continue
        if int(x):
            if x % 2 == 0:
                good.append(x)
            else:
                #print(f"{x} is odd")
                continue
        else:
            bad.append(i)
        #print(f"end of loop with {i}")
    good.sort(reverse=True)
    bad.sort()
    result=(good,bad)
    #print(f"the result is {result}")
    return result

if __name__ == '__main__':
    import doctest
    #doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True) # Shows all test output
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=False) # Runs test and only gives errors


z = '1 2 1 4 N/A MISSING 1'.split()
the_good_bad_and_sorted(z)
z = '100 85 37 50 N/A 66'.split()
the_good_bad_and_sorted(z)


#Python: Core Language Assessment - Intermediate Language Features - challenge_2.py 3/3/2025
from random import randint
class Power:

    def __init__(self, points, avatar):
        self.points = points
        self.avatar = avatar

    def activate(self, amplifier_callable: callable = randint):
        amplifier = amplifier_callable(1, 10)

        self.avatar = ' '.join([self.avatar] * amplifier)
        self.points *= amplifier

        return self.avatar, self.points

class Sparkle(Power):
    ''' Sparkle power is worth 2 points and has an avatar of 💥 '''
    def __init__(self):
        super().__init__()
        self.points = 2
        self.avatar = "💥"


class Shine(Power):
    ''' Shine power is worth 3 points and has an avatar of 🌞 '''
    def __init__(self):
        super().__init__()
        self.points = 3
        self.avatar = "🌞"


class SuperSlothBot:

    def __init__(self, name: str):
        '''
            Args:
                name    | The name of the bot.

        '''
        self.last_power = None
        self.name = name


    def activate(self, number: int):
        '''
            Args:
                number  | A randomly generated number between 0 and 50.

            Goal:
                Conditionally assign self.last_power to a Power object.
                    if the number is between  0-25  create a Sparkle object and assign it to self.last_power.
                    if the number is between 25-50  create a Shine   object and assign it to self.last_power.

                Once the last_power instance attribute is bound to the correct Power object:
                    Call the activate method and provide the randint_gen_callable class attribute as the argument.
                    Return the results from the call to last_power.activate.

            Raises:
                ValueError('number must be between 1-50')   | raised if number < 0 or number > 50

            >>> SuperSlothBot.randint_gen_callable = lambda *_: 5
            >>> for number in [20, 40]:
            ...     SuperSlothBot('bot 01').activate(number)
            ('💥 💥 💥 💥 💥', 10)
            ('🌞 🌞 🌞 🌞 🌞', 15)

            >>> sloth = SuperSlothBot('bot 01')
            >>> sloth.activate(10)
            ('💥 💥 💥 💥 💥', 10)

            >>> str(sloth)
            'bot 01 counjours: 💥 💥 💥 💥 💥 for a total of: 10 points.'

            >>> SuperSlothBot('bot 01').activate(-1)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50

            >>> SuperSlothBot('bot 01').activate(101)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50
        '''
        if number < 1 or number > 50:
            raise ValueError("number must be between 1-50")


def play(rounds=5):
    '''
        Make bots 1 and 2 fight.

        >>> from unittest.mock import MagicMock
        >>> randint_mock = MagicMock(side_effect=[40, 10, 20, 5, 20, 6, 30, 3])
        >>> SuperSlothBot.randint_gen_callable = randint_mock
        >>> play(2)
        ROUND 1, FIGHT!
        <BLANKLINE>
        ********************************************************************************
        bot 1 counjours: 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 for a total of: 30 points.
        bot 2 counjours: 💥 💥 💥 💥 💥 for a total of: 10 points.
        ********************************************************************************
        ROUND 2, FIGHT!
        <BLANKLINE>
        ********************************************************************************
        bot 1 counjours: 💥 💥 💥 💥 💥 💥 for a total of: 12 points.
        bot 2 counjours: 🌞 🌞 🌞 for a total of: 9 points.
        ********************************************************************************
        ________________________1st Place: Bot 1 With 42 Points!________________________
        ________________________2nd Place: Bot 2 With 19 Points!________________________
    '''
    bots = {
        1: SuperSlothBot('bot 1'),
        2: SuperSlothBot('bot 2'),
    }

    scores = {
        1: 0,
        2: 0,
    }


    for round in range(rounds):
        print(f'ROUND {round+1}, FIGHT!', end=f'\n\n{"*" * 80}\n')

        for n, bot in bots.items():
            bot.activate(SuperSlothBot.randint_gen_callable(0, 50))
            scores[n] += bot.last_power.points

        print(*[str(bot) for bot in bots.values()], sep='\n')
        print('*' * 80)

    # Sort by score descending.
    winners = sorted(scores.items(), key=lambda  _tuple: _tuple[1], reverse=True)
    one, two = winners

    # For the sake of this application ties are not handled. If there's a tie, one of these bots is going to get mad!
    print(f'''{''.join(('1st', f' place: {bots[one[0]].name} with {scores[one[0]]} points!'.title())):_^80}''')
    print(f'''{''.join(('2nd', f' place: {bots[two[0]].name} with {scores[two[0]]} points!'.title())):_^80}''')


if __name__ == '__main__':

    import doctest
    #doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True) # Shows all test output
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=False) # Runs test and only gives errors


#Python: Core Language Assessment - Intermediate Language Features - challenge_2.py 3/3/2025 (Progression)
from random import randint
class Power:

    def __init__(self, points, avatar):
        self.points = points
        self.avatar = avatar

    def activate(self, amplifier_callable: callable = randint):
        amplifier = amplifier_callable(1, 10)

        self.avatar = ' '.join([self.avatar] * amplifier)
        self.points *= amplifier
        #print(f"self.points: {self.points} * amplifier: {amplifier} = {self.points * amplifier}")
        return self.avatar, self.points


class Sparkle(Power):
    ''' Sparkle power is worth 2 points and has an avatar of 💥 '''
    def __init__(self):
        super().__init__(2,"💥")
        self.points = 2
        self.avatar = "💥"

class Shine(Power):
    ''' Shine power is worth 3 points and has an avatar of 🌞 '''
    def __init__(self):
        super().__init__(3,"🌞")
        self.points = 3
        self.avatar = "🌞"

class SuperSlothBot:
    randint_gen_callable = randint
    def __init__(self, name: str):
        '''
            Args:
                name    | The name of the bot.

        '''
        self.last_power = None
        self.name = name

    def activate(self, number: int):
        if number < 1 or number > 50:
            raise ValueError("number must be between 1-50")
        if number < 26:
            self.last_power = Sparkle()
        if number > 25:
            self.last_power = Shine()

        x = self.last_power.activate()
        #print(f"Class [SuperSlothBot(self)]:{self.name}, attribute [(self).last_power]:{self.last_power.avatar}, method [self.last_power.activate]= x:{x}")
        # Class [SuperSlothBot(self)]:<__main__.SuperSlothBot object at 0x0000020C3D92B050>, attribute [(self).last_power]:<__main__.Shine object at 0x0000020C3DAA1C50>, method [self.last_power.activate]= x:('🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞', 24)
        #print(f'''{''.join(('1st', f' place: {bots[one[0]].name} with {scores[one[0]]} points!'.title())):_^80}''')
        return x

    def __str__(self):
        try:
            return f'{self.name} counjours: {self.last_power.avatar} for a total of: {self.last_power.points} points.'
        except:
            return 'no power is currently activated'

        ''' 
            Args:
                number  | A randomly generated number between 0 and 50.
        
            Goal:
                Conditionally assign self.last_power to a Power object.
                    if the number is between  0-25  create a Sparkle object and assign it to self.last_power.
                    if the number is between 25-50  create a Shine   object and assign it to self.last_power.
                
                Once the last_power instance attribute is bound to the correct Power object:
                    Call the activate method and provide the randint_gen_callable class attribute as the argument.
                    Return the results from the call to last_power.activate.
            
            Raises:
                ValueError('number must be between 1-50')   | raised if number < 0 or number > 50

            >>> SuperSlothBot.randint_gen_callable = lambda *_: 5
            >>> for number in [20, 40]:
            ...     SuperSlothBot('bot 01').activate(number)
            ('💥 💥 💥 💥 💥', 10)
            ('🌞 🌞 🌞 🌞 🌞', 15)

            >>> sloth = SuperSlothBot('bot 01')
            >>> sloth.activate(10)
            ('💥 💥 💥 💥 💥', 10)

            >>> str(sloth)
            'bot 01 counjours: 💥 💥 💥 💥 💥 for a total of: 10 points.'

            >>> SuperSlothBot('bot 01').activate(-1)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50

            >>> SuperSlothBot('bot 01').activate(101)
            Traceback (most recent call last):
                ...
            ValueError: number must be between 1-50
        '''

def play(rounds=5):
    '''
        Make bots 1 and 2 fight.

        >>> from unittest.mock import MagicMock
        >>> randint_mock = MagicMock(side_effect=[40, 10, 20, 5, 20, 6, 30, 3])
        >>> SuperSlothBot.randint_gen_callable = randint_mock
        >>> play(2)
        ROUND 1, FIGHT!
        <BLANKLINE>
        ********************************************************************************
        bot 1 counjours: 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 🌞 for a total of: 30 points.
        bot 2 counjours: 💥 💥 💥 💥 💥 for a total of: 10 points.
        ********************************************************************************
        ROUND 2, FIGHT!
        <BLANKLINE>
        ********************************************************************************
        bot 1 counjours: 💥 💥 💥 💥 💥 💥 for a total of: 12 points.
        bot 2 counjours: 🌞 🌞 🌞 for a total of: 9 points.
        ********************************************************************************
        ________________________1st Place: Bot 1 With 42 Points!________________________
        ________________________2nd Place: Bot 2 With 19 Points!________________________
    '''
    bots = {
        1: SuperSlothBot('bot 1'),
        2: SuperSlothBot('bot 2'),
    }

    scores = {
        1: 0,
        2: 0,
    }


    for round in range(rounds):
        print(f'ROUND {round+1}, FIGHT!', end=f'\n\n{"*" * 80}\n')

        for n, bot in bots.items():
            bot.activate(SuperSlothBot.randint_gen_callable(0, 50))
            scores[n] += bot.last_power.points

        print(*[str(bot) for bot in bots.values()], sep='\n')
        print('*' * 80)

    # Sort by score descending.
    winners = sorted(scores.items(), key=lambda  _tuple: _tuple[1], reverse=True)
    one, two = winners

    # For the sake of this application ties are not handled. If there's a tie, one of these bots is going to get mad!
    print(f'''{''.join(('1st', f' place: {bots[one[0]].name} with {scores[one[0]]} points!'.title())):_^80}''')
    print(f'''{''.join(('2nd', f' place: {bots[two[0]].name} with {scores[two[0]]} points!'.title())):_^80}''')

if __name__ == '__main__':

    import doctest
    #doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=True) # Shows all test output
    doctest.testmod(optionflags=doctest.IGNORE_EXCEPTION_DETAIL, verbose=False) # Runs test and only gives errors





