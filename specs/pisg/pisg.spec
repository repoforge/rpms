# $Id: $

# Authority: dries
# Upstream: 

Summary: Perl script which generates statistics from IRC logfiles
Name: pisg
Version: 0.61
Release: 1
License: GPL
Group: Applications/Communications
URL: http://pisg.sourceforge.net/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://dl.sf.net/pisg/pisg-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# BuildRequires: 

%description
pisg is an IRC channel statics generator written in Perl, it creates
statistics from different logfile formats. It was originally written because
IRCStats wasn't open source. So here's an open source/GPL'ed version to
anyone interested. It's a funny thing for your IRC channel, and it's highly
customizeable.
Extensive documentation can be found at:
http://pisg.sourceforge.net/docs/

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_datadir}/pisg
%{__install} -d -m0755 %{buildroot}%{_bindir}
%{__cp} -R gfx layout modules pisg.cfg pisg lang.txt scripts %{buildroot}%{_datadir}/pisg
echo '%{_datadir}/pisg/pisg $@' > %{buildroot}%{_bindir}/pisg
%{__chmod} +x %{buildroot}%{_bindir}/pisg

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%doc docs
%{_bindir}/*
%config(noreplace) %{_datadir}/pisg/pisg.cfg
%{_datadir}/pisg

%changelog
* Sun Oct 31 2004 Dries Verachtert <dries@ulyssis.org> - 0.61-1
- Initial package.
