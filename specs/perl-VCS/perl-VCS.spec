# $Id$
# Authority: dries
# Upstream: Greg McCarroll <greg$mccarroll,org,uk>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name VCS

Summary: Library for generic Version Control System access in Perl
Name: perl-VCS
Version: 0.14
Release: 1.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/VCS/

Source: http://www.cpan.org/modules/by-module/VCS/VCS-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
`VCS' is an API for abstracting access to all version control systems
from Perl code. This is achieved in a similar fashion to the `DBI' suite
of modules. There are "container" classes, `VCS::Dir', `VCS::File', and
`VCS::Version', and "implementation" classes, such as `VCS::Cvs::Dir',
`VCS::Cvs::File', and `VCS::Cvs::Version', which are subclasses of their
respective "container" classes.

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
%doc Changes README
%{_bindir}/diff-hist
%doc %{_mandir}/man?/*
%{perl_vendorlib}/VCS.pm
%{perl_vendorlib}/VCS/*
%{perl_vendorlib}/VCS_dev.pod

%changelog
* Wed Mar 22 2006 Dries Verachtert <dries@ulyssis.org> - 0.14-1.2
- Rebuild for Fedora Core 5.

* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - 0.14-1
- Initial package.
