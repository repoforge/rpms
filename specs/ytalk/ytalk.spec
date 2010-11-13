# $Id$
# Authority: nac

### EL2 ships with ytalk-3.1.1-7
%{?el2:# Tag: rfx}

Summary: Enhanced replacement for the BSD talk client
Name: ytalk
Version: 3.3.0
Release: 1.0%{?dist}
License: GPL
Group: Applications/Communications
URL: http://www.impul.se/ytalk/

Source: http://www.impul.se/ytalk/ytalk-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: ncurses-devel

%description
Talk is a compatible replacement for the BSD talk(1) program.

The main advantage of YTalk is the ability to communicate with any arbitrary
number of users at once. It supports both talk protocols ("talk" and
"ntalk") and can communicate with several different talk daemons at the same
time.

You may also spawn a command shell in your talk window and let other users
watch. YTalk supports a basic set of VT100 control codes, as well as job
control (BSD support added in 3.1.3)

%prep
%setup

%build
%configure
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL README
%doc %{_mandir}/man1/ytalk.1*
%config(noreplace) %{_sysconfdir}/ytalkrc
%{_bindir}/ytalk

%changelog
* Thu Jul 28 2005 Wil Cooley <wcooley@nakedape.cc> - 3.3.0-1
- Initial package creation
