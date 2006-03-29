# $Id$
# Authority: dries
# Upstream: Dominik Seichter <domseichter$web,de>

Summary: Batch file renamer
Name: krename
Version: 3.0.11
Release: 1
License: GPL
Group: Applications/Utilities
URL: http://www.krename.net/

Source: http://dl.sf.net/krename/krename-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: kdelibs-devel, gcc-c++, gettext

%description
Krename is a very powerful batch file renamer for KDE3 which can rename a
list of files based on a set of expressions. It can copy/move the files to
another directory or simply rename the input files. Krename supports many
conversion operations, including conversion of a filename to lowercase or
to uppercase, conversion of the first letter of every word to uppercase,
adding numbers to filenames, finding and replacing parts of the filename,
and many more. It can also change access and modification dates,
permissions, and file ownership.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%{_bindir}/krename
%{_datadir}/icons/*/*/apps/krename.png
%{_datadir}/doc/HTML/en/krename/
%{_datadir}/apps/krename/
%{_datadir}/services/krename*.desktop
%{_datadir}/applications/kde/krename.desktop

%changelog
* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.11-1
- Updated to release 3.0.11.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.10-1
- Initial package.
