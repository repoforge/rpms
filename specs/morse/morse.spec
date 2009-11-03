# $Id$
# Authority: dag

Summary: Morse Classic morse trainer program
Name: morse
Version: 2.1
Release: 1%{?dist}
License: BSD
Group: Applications/Communications
URL: http://catb.org/~esr/morse/

Source: http://catb.org/~esr/morse/morse-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description 
Morse Classic is a Morse-code training program for aspiring radio hams.  It
can generate random tests or simulated QSOs resembling those used in
the ARRL test (a QSO generator is included).  There are a plethora of
options to vary the training method.  In one of the simpler modes,
this program will take text from standard input and render it as
Morse-code beeps.

%prep
%setup

%build
%{__make} %{?_smp_mflags} morse QSO morse.1 QSO.1

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 morse %{buildroot}%{_bindir}/morse
%{__install} -Dp -m0755 QSO %{buildroot}%{_bindir}/QSO
%{__install} -Dp -m0644 morse.1 %{buildroot}%{_mandir}/man1/morse.1
%{__install} -Dp -m0644 QSO.1 %{buildroot}%{_mandir}/man1/QSO.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc HISTORY README
%defattr(-, root, root, 0755)
%doc %{_mandir}/man1/morse.1*
%doc %{_mandir}/man1/QSO.1*
%{_bindir}/morse
%{_bindir}/QSO

%changelog
* Fri Feb 23 2007 Dag Wieers <dag@wieers.com> - 2.1-1
- Initial package. (using DAR)
