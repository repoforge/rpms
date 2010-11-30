# $Id$
# Authority: shuff
# Upstream: Andy Lester <mopy$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name HTML-Tidy

Summary: (X)HTML validation in a Perl object
Name: perl-%{real_name}
Version: 1.54
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/HTML-Tidy/

Source: http://search.cpan.org/CPAN/authors/id/P/PE/PETDANCE/HTML-Tidy-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 5.8
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(constant)
BuildRequires: perl(overload)
BuildRequires: rpm-macros-rpmforge
BuildRequires: tidyp-devel
Requires: perl >= 5.8
Requires: perl(Carp)
Requires: perl(Exporter)
Requires: perl(constant)
Requires: perl(overload)
Requires: tidyp


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
HTML::Tidy is an HTML checker in a handy dandy object.

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
%doc Changes MANIFEST META.yml README.markdown
%doc %{_mandir}/man?/*
%dir %{perl_vendorarch}/HTML/
%{perl_vendorarch}/HTML/Tidy.pm
%{perl_vendorarch}/HTML/Tidy/
%{perl_vendorarch}/auto/HTML/Tidy/
%{_bindir}/*

%changelog
* Tue Nov 30 2010 Steve Huff <shuff@vecna.org> - 1.54-1
- Initial package.
