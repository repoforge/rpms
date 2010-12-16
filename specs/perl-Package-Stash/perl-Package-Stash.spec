# $Id$
# Authority: shuff
# Upstream: Jesse Luehrs <doy$tozt,net>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Package-Stash

Summary: Routines for manipulating stashes
Name: perl-Package-Stash
Version: 0.13
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Package-Stash/

Source: http://search.cpan.org/CPAN/authors/id/D/DO/DOY/Package-Stash-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)%{?!el5: >= 6.31}
BuildRequires: perl(Scalar::Util)
# BuildRequires: perl(Test::Fatal)
# BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Scalar::Util)

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
Manipulating stashes (Perl's symbol tables) is occasionally necessary, but
incredibly messy, and easy to get wrong. This module hides all of that behind a
simple API.

%prep
%setup -n %{real_name}-%{version}

# damn it Dist::Zilla
%{?el5:%{__perl} -pi -e '/.*ExtUtils::MakeMaker.*6.31.*/ && s/6\.3\d/6.30/' Makefile.PL}

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
%doc Changes META.json LICENSE README
%doc %{_mandir}/man?/*
%{perl_vendorlib}/Package/Stash.pm
#%{perl_vendorlib}/Package/Stash/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Dec 16 2010 Steve Huff <shuff@vecna.org> - 0.13-1
- Initial package.
