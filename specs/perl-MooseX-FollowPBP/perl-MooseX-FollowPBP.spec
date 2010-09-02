# $Id$
# Authority: shuff
# Upstream: Dave Rolsky <autarch$urth,org>
# ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-FollowPBP

Summary: Name your accessors get_foo() and set_foo()
Name: perl-MooseX-FollowPBP
Version: 0.04
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-FollowPBP/

Source: http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/MooseX-FollowPBP-%{version}.tar.gz
Patch0: perl-MooseX-FollowPBP_ExtUtils-MakeMaker.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
# BuildRequires: perl(ExtUtils::MakeMaker) >= 6.31
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Moose) >= 0.94
# BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(Test::More)
BuildRequires: rpm-macros-rpmforge
Requires: perl
Requires: perl(Moose) >= 0.94

### remove autoreq Perl dependencies
%filter_from_requires /^perl.*/d
%filter_setup

%description
This module does not provide any methods. Simply loading it changes the default
naming policy for the loading class so that accessors are separated into get
and set methods. The get methods are prefixed with "get_" as the accessor,
while set methods are prefixed with "set_". This is the naming style
recommended by Damian Conway in Perl Best Practices.

If you define an attribute with a leading underscore, then both the get and set
method will also have an underscore prefix.

If you explicitly set a "reader" or "writer" name when creating an attribute,
then that attribute's naming scheme is left unchanged.

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
%doc Changes INSTALL LICENSE META.json README SIGNATURE
%doc %{_mandir}/man?/*
%{perl_vendorlib}/MooseX/FollowPBP.pm
%{perl_vendorlib}/MooseX/FollowPBP/*
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Sep 02 2010 Steve Huff <shuff@vecna.org> - 0.04-1
- Initial package.
