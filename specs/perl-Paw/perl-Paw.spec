# $Id$
# Authority: dag
# Upstream: Uwe Gansert <ug$suse,de>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Paw

Summary: Perl module named Paw
Name: perl-Paw
Version: 0.54
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Paw/

Source: http://www.cpan.org/authors/id/U/UG/UGANSERT/Paw-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Paw is a Perl module.

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
%doc Changes.txt INSTALL INSTALL-DE LICENSE MANIFEST
%{perl_vendorlib}/Paw/
%{perl_vendorlib}/Paw.pm

%changelog
* Sun Oct 07 2007 Dag Wieers <dag@wieers.com> - 0.54-1
- Initial package. (using DAR)
