# $Id$
# Authority: shuff
# Upstream: Dave Cross <dave$mag-sol,com>

## This package needs Moose.
## ExcludeDist: el3 el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Parse-RPM-Spec

Summary: Perl extension to parse RPM spec files
Name: perl-%{real_name}
Version: 0.03
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Parse-RPM-SPEC/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DAVECROSS/Parse-RPM-Spec-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(ExtUtils::MakeMaker)

%description
RPM is the package management system used on Linux distributions based on Red
Hat Linux. These days that includes Fedora, Red Hat Enterprise Linux, Centos,
SUSE, Mandriva and many more.

RPMs are build from the source of a packages along with a spec file. The spec
file controls how the RPM is built.

This module creates Perl objects which module spec files. Currently it gives
you simple access to various pieces of information from the spec file.

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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Parse::RPM::Spec.3pm*
%dir %{perl_vendorlib}/Parse/RPM/
%{perl_vendorlib}/Parse/RPM/Spec.pm

%changelog
* Fri Oct 02 2009 Steve Huff <shuff@vecna.org> - 0.03-1
- Initial package.
