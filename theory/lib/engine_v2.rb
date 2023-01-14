module EngineV2
  extend self

  SIMPLIFICATIONS = {
    'A##' => 'B',
    'B##' => 'C#',
    'C##' => 'D',
    'D##' => 'E',
    'E##' => 'F#',
    'F##' => 'G',
    'G##' => 'A',
    'Bbb' => 'A',
    'Ebb' => 'D',
    'Abb' => 'G',
    'Dbb' => 'C',
    'Gbb' => 'F',
    'Cbb' => 'Bb',
    'Fbb' => 'Eb',
  }

  def up(note)
    up = case note
         when 'B'
           'C'
         when 'E'
           'F'
         else
           if note.include?('b')
             note[0..-2]
           else
             "#{note}#"
           end
         end

    simplify(up)
  end

  def down(note)
    down = case note
           when 'C'
             'B'
           when 'F'
             'E'
           else
             if note.include?('#')
               note[0..-2]
             else
               "#{note}b"
             end
           end

    simplify(down)
  end

  private

  def simplify(note)
    SIMPLIFICATIONS[note] || note
  end
end
