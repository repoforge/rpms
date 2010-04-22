# $Id$
# Authority: shuff
# Upstream: Jonny Shulz <jshulz$bloonix,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Log-Handler

Summary: Log messages to several outputs
Name: perl-%{real_name}
Version: 0.64
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Log-Handler/

Source: http://search.cpan.org/CPAN/authors/id/B/BL/BLOONIX/Log-Handler-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Fcntl)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Module::Build)
BuildRequires: perl(POSIX)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Sys::Hostname)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::HiRes)
BuildRequires: perl(UNIVERSAL)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Config::General)
Requires: perl(Config::Properties)
Requires: perl(Data::Dumper)
Requires: perl(DBI)
Requires: perl(Email::Date)
Requires: perl(Fcntl)
Requires: perl(File::Spec)
Requires: perl(IO::Socket)
Requires: perl(Net::SMTP)
Requires: perl(POSIX)
Requires: perl(Params::Validate)
Requires: perl(Sys::Hostname)
Requires: perl(Time::HiRes)
Requires: perl(UNIVERSAL)
Requires: perl(YAML)


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
The Log::Handler is a object oriented handler for logging, tracing and
debugging. It is very easy to use and provides a simple interface for multiple
output objects with lots of configuration parameters. You can easily filter the
amount of logged information on a per-output base, define priorities, create
patterns to format the messages and reload the complete logging machine.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog INSTALL LICENCE MANIFEST README
%doc examples/
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Log/
%{perl_vendorlib}/Log/Handler.pm
%{perl_vendorlib}/Log/Handler/*

%changelog
* Thu Apr 22 2010 Steve Huff <shuff@vecna.org> - 0.64-1
- Initial package.
