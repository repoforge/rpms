# $Id$
# Authority: shuff
# Upstream: Tokuhiro Matsuno <tokuhirom$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-TCP

Summary: test TCP programs
Name: perl-Test-TCP
Version: 1.12
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-TCP/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOKUHIROM/Test-TCP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 5.8.0
BuildRequires: perl(Carp)
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::Socket::INET)
BuildRequires: perl(POSIX)
BuildRequires: perl(Test::SharedFork) >= 0.14
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.0
Requires: perl(Carp)
Requires: perl(Config)
Requires: perl(IO::Socket::INET)
Requires: perl(POSIX)
Requires: perl(Test::SharedFork) >= 0.14
Requires: perl(Test::More)
Requires: perl(Time::HiRes)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Test::TCP contains test utilities for TCP programs.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
#%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

# fix for stupid strip issue
#%{__chmod} -R u+w %{buildroot}/*

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Test/TCP.pm
#%{perl_vendorlib}/Test/TCP/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist
# perl_privlib: /usr/lib/perl5/5.8.0

%changelog
* Fri May 20 2011 Steve Huff <shuff@vecna.org> - 1.12-1
- Initial package.
