# $Id$
# Authority: shuff
# Upstream: Shawn M. Moore <sartak$gmail,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Role-Parameterized

Summary: Roles with composition parameters
Name: perl-%{real_name}
Version: 0.14
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Role-Parameterized/

Source: http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/MooseX-Role-Parameterized-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: perl >= 5.8.1
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Exception) >= 0.27
BuildRequires: perl(Test::Moose)
#BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl >= 5.8.1
Requires: perl(Moose) >= 0.78


### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Roles are composable units of behavior. They are useful for factoring out
functionality common to many classes from any part of your class hierarchy. See
Moose::Cookbook::Roles::Recipe1 for an introduction to Moose::Role.

While combining roles affords you a great deal of flexibility, individual roles
have very little in the way of configurability. Core Moose provides alias for
renaming methods and excludes for ignoring methods. These options are primarily
(perhaps solely) for disambiguating role conflicts. See
Moose::Cookbook::Roles::Recipe2 for more about alias and excludes.

Because roles serve many different masters, they usually provide only the least
common denominator of functionality. To empower roles further, more
configurability than alias and excludes is required. Perhaps your role needs to
know which method to call when it is done. Or what default value to use for its
url attribute.

Parameterized roles offer exactly this solution.

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
%doc Changes MANIFEST META.yml
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/MooseX/Role/
%{perl_vendorlib}/MooseX/Role/*

%changelog
* Fri Dec 18 2009 Steve Huff <shuff@vecna.org> - 0.14-1
- Initial package.
