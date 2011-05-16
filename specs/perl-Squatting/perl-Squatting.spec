# $Id$
# Authority: shuff
# Upstream: John Beppu <beppu$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Squatting

Summary: A Camping-inspired Web Microframework for Perl
Name: perl-%{real_name}
Version: 0.81
Release: 1%{?dist}
License: MIT
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Squatting/

Source: http://search.cpan.org/CPAN/authors/id/B/BE/BEPPU/Squatting-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl
BuildRequires: perl(Class::C3::Componentised)
BuildRequires: perl(Clone)
BuildRequires: perl(Continuity) >= 0.991
BuildRequires: perl(Data::Dump)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(HTTP::Daemon)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(IO::All)
BuildRequires: perl(JSON::XS)
BuildRequires: perl(Shell::Perl)
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Class::C3::Componentised)
Requires: perl(Clone)
Requires: perl(Continuity) >= 0.991
Requires: perl(Data::Dump)
Requires: perl(HTTP::Daemon)
Requires: perl(HTTP::Response)
Requires: perl(IO::All)
Requires: perl(JSON::XS)
Requires: perl(Shell::Perl)
Requires: rpm-macros-rpmforge


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Squatting is a web microframework based on Camping. It originally used
Continuity as its foundation, but it has since been generalized such that it
can squat on top of any Perl-based web framework (in theory).

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
%doc Changes MANIFEST META.yml README doc/ eg/
%doc %{_mandir}/man?/*
%{perl_vendorlib}/squatting.pl
%{perl_vendorlib}/Squatting.pm
%{perl_vendorlib}/Squatting/*
%{_bindir}/*

%changelog
* Mon May 16 2011 Steve Huff <shuff@vecna.org> - 0.81-1
- Updated to release 0.81.
- Included the examples in the docdir.

* Mon Jan 04 2010 Steve Huff <shuff@vecna.org> - 0.70-1
- Initial package.
