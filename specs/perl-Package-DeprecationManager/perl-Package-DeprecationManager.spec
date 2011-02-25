# $Id$
# Authority: shuff
# Upstream: Dave Rolsky <autarch$urth,org>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Package-DeprecationManager

Summary: Manage deprecation warnings for your distribution
Name: perl-Package-DeprecationManager
Version: 0.10
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Package-DeprecationManager/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Package-DeprecationManager-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Carp)
BuildRequires: perl(List::MoreUtils)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Sub::Install)
# BuildRequires: perl(Test::Fatal)
# BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
# BuildRequires: perl(Test::Requires)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Carp)
Requires: perl(List::MoreUtils)
Requires: perl(Params::Util)
Requires: perl(Sub::Install)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module allows you to manage a set of deprecations for one or more modules.

When you import Package::DeprecationManager, you must provide a set of
-deprecations as a hash ref. The keys are "feature" names, and the values are
the version when that feature was deprecated.

In many cases, you can simply use the fully qualified name of a subroutine or
method as the feature name. This works for cases where the whole subroutine is
deprecated. However, the feature names can be any string. This is useful if you
don't want to deprecate an entire subroutine, just a certain usage.

%prep
%setup -n %{real_name}-%{version}

%build
# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6\.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes INSTALL LICENSE META.json README SIGNATURE
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Package/DeprecationManager.pm
#%{perl_vendorlib}/Package/DeprecationManager/*
#%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Fri Feb 25 2011 Steve Huff <shuff@vecna.org> - 0.10-1
- Initial package.
