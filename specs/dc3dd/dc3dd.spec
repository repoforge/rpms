# $Id$
# Authority: dag


%{?el3:%define _without_gettextdevel 1}
%{?rh9:%define _without_gettextdevel 1}
%{?rh7:%define _without_gettextdevel 1}
%{?el2:%define _without_gettextdevel 1}

Summary: Patched dd with Computer Forensics Features
Name: dc3dd
Version: 6.12.3
Release: 1%{?dist}
License: GPL
Group: Applications/System
URL: http://dc3dd.sourceforge.net/

Source: http://dl.sf.net/sourceforge/dc3dd/dc3dd-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%{!?_without_gettextdevel:BuildRequires: gettext-devel}
%{?_without_gettextdevel:BuildRequires: gettext}

%description
dc3dd is a patched version of GNU dd to include a number of features useful
for computer forensics. Many of these features were inspired by dcfldd, but
were rewritten for dc3dd.

* Pattern writes. The program can write a single hexadecimal value or a text
  string to the output device for wiping purposes.
* Piecewise and overall hashing with multiple algorithms and variable size
  windows. Supports MD5, SHA-1, SHA-256, and SHA-512. Hashes can be computed
  before or after conversions are made.
* Progress meter with automatic input/output file size probing
* Combined log for hashes and errors
* Error grouping. Produces one error message for identical sequential errors
* Verify mode. Able to repeat any transformations done to the input file and
  compare it to an output.
* Ability to split the output into chunks with numerical or alphabetic
  extensions

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING NEWS README THANKS THANKS-to-translators *.txt
%doc %{_mandir}/man1/dc3dd.1*
%{_bindir}/dc3dd

%changelog
* Mon Mar 23 2009 Dag Wieers <dag@wieers.com> - 6.12.3-1
- Updated to release 6.12.3.

* Wed Nov 12 2008 Dag Wieers <dag@wieers.com> - 6.12.2-1
- Updated to release 6.12.2.

* Sat Nov 08 2008 Dag Wieers <dag@wieers.com> - 6.12.1-1
- Initial package. (using DAR)
