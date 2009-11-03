# $Id$
# Authority: nac

Summary: Pre-loadable library for faking the system date
Name: libfaketime
Version: 0.5
Release: 1%{?dist}
License: GPL
Group: System Environment/Libraries
URL: http://www.code-wizards.com/projects/libfaketime/

Source: http://www.code-wizards.com/projects/libfaketime/libfaketime-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
FTPL intercepts various system calls which programs use to retrieve the
current date and time. It can then report faked dates and times (as
specified by you, the user) to these programs. This means you can modify the
system time a program sees without changing the time system-wide.

FTPL allows you to specify both absolute dates (e.g., 1.1.2004) and relative
dates (e.g., 10 days ago).

FTPL can be used for running legacy software with y2k bugs, testing software
for year-2038 compliance, debugging time-related issues or run software which
ceases to run outside a certain timeframe

%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 libfaketime.so.1 %{buildroot}/%{_libdir}/libfaketime/libfaketime.so.1
%{__install} -Dp -m0755 timetest %{buildroot}/%{_bindir}/faketimetest

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changelog COPYING README
%{_libdir}/libfaketime/*
%{_bindir}/faketimetest

%changelog
* Tue Sep 26 2006 Dries Verachtert <dries@ulyssis.org> - 0.5-1
- Updated to release 0.5.

* Wed Jul 27 2005 Wil Cooley <wcooley@nakedape.cc> - 0.3-1.0
- Initial package creation.
