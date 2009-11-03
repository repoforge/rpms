# $Id$

# Authority: dag
# Upstream: <childsplay$linux,isbeter,nl>

Summary: Games for children with plugins
Name: childsplay
Version: 0.81.1
Release: 1%{?dist}
License: GPL
Group: Amusements/Games
URL: http://childsplay.sourceforge.net/

Source: http://dl.sf.net/childsplay/%{name}-%{version}.tar.gz
Source1: http://dl.sf.net/childsplay/%{name}-plugins-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: python-devel, python
Requires: python-game, libogg
Requires: SDL >= 1.2, SDL_image >= 1.2, SDL_mixer >= 1.2
#Requires: SDL_ttf >= 1.2

%description
Childsplay is a 'suite' of educational games for young children. It's written
in Python and uses the SDL-libraries to make it more games-like then, for
instance, gcompris. The aim is to be educational and at the same time be fun
to play.

NOTE: This package also requires the childsplay-plugins package.

%prep
%setup -a1 -n %{name}-%{version}

### fix python compile error
%{__perl} -pi.orig -e 's|quiet\=1||g' install.py

%{__cat} <<'EOF' >childsplay.sh
#!/bin/sh
exec python %{_libdir}/childsplay/childsplay.py $@
EOF

%build
%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/childsplay/lib/LettersData/ \
			%{buildroot}%{_libdir}/childsplay/MemoryData/ \
			%{buildroot}%{_datadir}/locale/
%{__install} -Dp -m0755 childsplay.sh %{buildroot}%{_bindir}/childsplay
%{__install} -Dp -m0644 man/childsplay.6.gz %{buildroot}%{_mandir}/man6/childsplay.6.gz
%{__cp} -fpr *.py %{buildroot}%{_libdir}/childsplay/
%{__cp} -fpr Data/ %{buildroot}%{_libdir}/childsplay/
%{__cp} -fpr lib %{buildroot}%{_libdir}/childsplay/
%{__cp} -fpr locale/* %{buildroot}%{_datadir}/locale/

### compile bytecode
python install.py --compile %{buildroot}%{_libdir}/childsplay/
#python install.py --compile %{buildroot}%{_libdir}/childsplay/
python install.py --makedir %{buildroot}%{_libdir}/childsplay/

### fix symlinks
%{__rm} -f %{buildroot}%{_libdir}/childsplay/lib/LettersData/*
%{__cp} -p %{buildroot}%{_libdir}/childsplay/lib/MemoryData/* %{buildroot}%{_libdir}/childsplay/lib/LettersData/

### install plugins
cd %{name}-plugins-%{version}/
python %{buildroot}%{_libdir}/childsplay/install.py --compile Lib
%{__cp} -fpr Lib/* %{buildroot}%{_libdir}/childsplay/lib/
%{__cp} -fpr Data/*.icon.png %{buildroot}%{_libdir}/childsplay/Data/icons/
%{__cp} -fpr locale/* %{buildroot}%{_datadir}/locale/
python add-score.py %{buildroot}%{_libdir}/childsplay/ "Packid,Numbers"
cd -

%find_lang %{name}
#%find_lang letters %{name}.lang
#%find_lang memory %{name}.lang
%find_lang letters
%find_lang memory
%find_lang numbers
%find_lang packid
%find_lang soundNpic
%{__cat} letters.lang memory.lang numbers.lang packid.lang soundNpic.lang >>%{name}.lang

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc README* doc/GPL* doc/README*
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/childsplay/
%defattr(-, root, root, 0666)
%dir %{_libdir}/childsplay/Data/score/

%changelog
* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 0.81.1-1
- Updated to release 0.81.1.

* Mon Nov 17 2003 Dag Wieers <dag@wieers.com> - 0.69-0
- Updated to release 0.69.

* Thu Sep 04 2003 Dag Wieers <dag@wieers.com> - 0.68-0
- Initial package. (using DAR)
