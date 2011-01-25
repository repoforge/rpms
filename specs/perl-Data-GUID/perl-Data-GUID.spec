# $Id$
# Authority: shuff
# Upstream: Ricardo Signes <rjbs$cpan,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Data-GUID

Summary: globally unique identifiers
Name: perl-Data-GUID
Version: 0.046
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Data-GUID/

Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Data-GUID-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Data::UUID) >= 1.148
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Sub::Exporter) >= 0.90
BuildRequires: perl(Sub::Install) >= 0.03
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Data::UUID) >= 1.148
Requires: perl(Sub::Exporter) >= 0.90
Requires: perl(Sub::Install) >= 0.03

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Data::GUID provides a simple interface for generating and using globally unique
identifiers.

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
%doc Changes META.yml README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Data/GUID.pm
#%{perl_vendorlib}/Data/GUID/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Tue Jan 25 2011 Steve Huff <shuff@vecna.org> - 0.046-1
- Initial package.
