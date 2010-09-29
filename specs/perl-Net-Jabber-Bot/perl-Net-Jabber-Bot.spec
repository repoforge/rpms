# $Id$
# Authority: shuff
# Upstream: Todd E. Rinaldo <perl-net-jabber-bot$googlegroups,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Net-Jabber-Bot

Summary: Automated Bot creation with safeties
Name: perl-Net-Jabber-Bot
Version: 2.1.5
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-Jabber-Bot/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Net-Jabber-Bot-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FindBin)
BuildRequires: perl(Log::Log4perl)
BuildRequires: perl(Moose) >= 0.82
BuildRequires: perl(MooseX::Types) >= 0.12
BuildRequires: perl(Net::Jabber) >= 2
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::More)
BuildRequires: perl(Test::NoWarnings)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(lib)
BuildRequires: perl(version)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(FindBin)
Requires: perl(Log::Log4perl)
Requires: perl(Moose) >= 0.82
Requires: perl(MooseX::Types) >= 0.12
Requires: perl(Net::Jabber) >= 2
Requires: perl(Sys::Hostname)
Requires: perl(Time::HiRes)
Requires: perl(lib)
Requires: perl(version)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The idea behind the module is that someone creating a bot should not really
have to know a whole lot about how the Jabber protocol works in order to use
it. It also allows us to abstract away all the things that can get a bot maker
into trouble. Essentially the object helps protect the coders from their own
mistakes.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install
#%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes META.yml README examples/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Net/Jabber/Bot.pm
#%{perl_vendorlib}/Net/Jabber/Bot/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Wed Sep 29 2010 Steve Huff <shuff@vecna.org> - 2.1.5-1
- Initial package.
