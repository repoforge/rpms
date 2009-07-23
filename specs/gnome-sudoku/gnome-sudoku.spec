# $Id$
# Authority: dag

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

%define desktop_vendor rpmforge

Summary: Sudoku, a logic puzzle game
Name: gnome-sudoku
Version: 0.7.1
Release: 2
License: GPL
Group: Amusements/Games
URL: http://gnome-sudoku.sourceforge.net/

Source: http://dl.sf.net/gnome-sudoku/gnome-sudoku-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: gnome-python2-gnomeprint
BuildRequires: intltool
BuildRequires: pygtk2-libglade
BuildRequires: python-devel >= 2.4
BuildRequires: python-imaging
Requires: gnome-python2-canvas
Requires: gnome-python2-gconf
Requires: gnome-python2-gnomeprint
Requires: pygtk2-libglade
Requires: python >= 2.4
Requires: python-imaging
Requires: python-numeric

%description
GNOME Sudoku is a Japanese logic puzzle game. GNOME Sudoku takes care
to generate valid sudoku -- symmetrical puzzles for which there is a
unique solution.

%prep
%setup
grep '^VERSION' src/lib/defaults.py >src/lib/defaults_version.py


%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

desktop-file-install --delete-original         \
    --vendor %{desktop_vendor}                 \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/gnome-sudoku.desktop

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc COPYING README
%doc %{_datadir}/gnome/help/gnome-sudoku/
%{_bindir}/gnome-sudoku
%{_datadir}/applications/%{desktop_vendor}-gnome-sudoku.desktop
%{_datadir}/gnome-sudoku/
%{_datadir}/pixmaps/gnome-sudoku/
%{_datadir}/pixmaps/sudoku.png
%{python_sitelib}/gnome_sudoku/

%changelog
* Tue Jul 21 2009 Dag Wieers <dag@wieers.com> - 0.7.1-2
- Rebuild after correcting %%{desktop_vendor}.

* Fri Nov 23 2007 Dag Wieers <dag@wieers.com> - 0.7.1-1
- Initial package. (using DAR)
