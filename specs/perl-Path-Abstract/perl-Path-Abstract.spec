# $Id$
# Authority: shuff
# Upstream: Robert Krimen <robertkrimen$gmail,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Path-Abstract

Summary: Fast and featureful UNIX-style path parsing and manipulation
Name: perl-Path-Abstract
Version: 0.096
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Path-Abstract/

Source: http://search.cpan.org/CPAN/authors/id/R/RO/ROKR/Path-Abstract-%{version}.tar.gz
Patch0: perl-Path-Abstract-0.096_ExtUtilsMakeMaker.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
# BuildRequires: perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Sub::Exporter)
# BuildRequires: perl(Test::Lazy)
BuildRequires: perl(Test::More)
# BuildRequires: perl(Test::Most)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(Scalar::Util)
Requires: perl(Sub::Exporter)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Path::Abstract is a tool for parsing, interrogating, and modifying a UNIX-style
path. The parsing behavior is similar to File::Spec::Unix, except that trailing
slashes are preserved (converted into a single slash).

%prep
%setup -n %{real_name}-%{version}
%patch0 -p1

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
%{perl_vendorlib}/Path/Abstract.pm
%{perl_vendorlib}/Path/Abstract/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Aug 26 2010 Steve Huff <shuff@vecna.org> - 0.096-1
- Initial package.
