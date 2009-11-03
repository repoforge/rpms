# $Id$
# Authority: dag
# Upstream: Ken MacLeod <ken$bitsko,slc,ut,us>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Quilt

Summary: Perl module named Quilt
Name: perl-Quilt
Version: 0.08
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Quilt/

Source: http://www.cpan.org/authors/id/K/KM/KMACLEOD/Quilt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Quilt is a Perl module.

This package contains the following Perl module:

    Quilt

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
%doc COPYING ChangeLog Changes MANIFEST README ToDo
%{perl_vendorlib}/Quilt/
%{perl_vendorlib}/Quilt.pm

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
