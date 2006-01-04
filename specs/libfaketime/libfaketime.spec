# $Id$
# Authority: nac

Summary:        Pre-loadable library for faking the system date.
Name:           libfaketime
Version:        0.3
Release:        1.0
License:        GPL
Group:          System Environment/Libraries
Source:         http://www.code-wizards.com/projects/libfaketime/libfaketime-%{version}.tar.gz
URL:            http://www.code-wizards.com/projects/libfaketime/index.html  
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description

FTPL intercepts various system calls which programs use to retrieve the
current date and time. It can then report faked dates and times (as
specified by you, the user) to these programs. This means you can modify the
system time a program sees without changing the time system-wide.

FTPL allows you to specify both absolute dates (e.g., 1.1.2004) and relative
dates (e.g., 10 days ago).

FTPL might be used for various purposes, for example

    * running legacy software with y2k bugs
    * testing software for year-2038 compliance
    * debugging time-related issues
    * run software which ceases to run outside a certain timeframe 

Compatibility issues

    * FTPL has been designed on and for Linux, but is supposed to work on
    other *NIXes as well.

    * FTPL uses the library preload mechanism and thus cannot work with
    statically linked binaries.

%prep
%setup

%build
%{__make}

%install
%{__rm} -rf %{buildroot}
%{__install} -d %{buildroot}/%{_libdir}/%{name}/
%{__install} -d %{buildroot}/%{_bindir}
%{__install} -m 0755 libfaketime.so.1 %{buildroot}/%{_libdir}/%{name}/
%{__install} -m 0755 timetest %{buildroot}/%{_bindir}/faketimetest

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%{_libdir}/%{name}/*
%{_bindir}/*
%doc COPYING Changelog README

%changelog
* Wed Jul 27 2005 Wil Cooley <wcooley@nakedape.cc> - 0.3-1.0
- Initial package creation.
