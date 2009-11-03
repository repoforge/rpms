# $Id$
# Authority: dries
# Upstream: Dominik Seichter <domseichter$web,de>

Summary: Batch file renamer
Name: krename
Version: 3.0.14
Release: 2%{?dist}
License: GPL
Group: Applications/File
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
%configure LDFLAGS=-L$QTLIB
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README TODO
%doc %{_datadir}/doc/HTML/en/krename/
%{_bindir}/krename
%{_datadir}/icons/*/*/apps/krename.png
%{_datadir}/apps/krename/
%{_datadir}/apps/konqueror/servicemenus/krename*.desktop
%{_datadir}/applications/kde/krename.desktop

%changelog
* Tue Apr 24 2007 Dag Wieers <dag@wieers.com> - 3.0.14-2
- Fix group tag.

* Sun Apr 01 2007 Dries Verachtert <dries@ulyssis.org> - 3.0.14-1
- Updated to release 3.0.14.

* Sun Dec 03 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.13-1
- Updated to release 3.0.13.

* Tue Aug 15 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.12-1
- Updated to release 3.0.12.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.11-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.11-1
- Updated to release 3.0.11.

* Sat Jan 14 2006 Dries Verachtert <dries@ulyssis.org> - 3.0.10-1
- Initial package.
