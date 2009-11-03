# $Id$
# Authority: dag
# Upstream: John Cerney <j-cerney1$raytheon,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Tk-TableMatrix

Summary: Perl module named Tk-TableMatrix
Name: perl-Tk-TableMatrix
Version: 1.23
Release: 1%{?dist}
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Tk-TableMatrix/

Source: http://www.cpan.org/modules/by-module/Tk/Tk-TableMatrix-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Tk::MMtry)

%description
perl-Tk-TableMatrix is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/Tk/
%{perl_vendorarch}/Tk/pTk/
%{perl_vendorarch}/Tk/TableMatrix.pm
%{perl_vendorarch}/Tk/TableMatrix.pod
%{perl_vendorarch}/Tk/TableMatrix/
%dir %{perl_vendorarch}/auto/Tk/
%{perl_vendorarch}/auto/Tk/pTk/
%{perl_vendorarch}/auto/Tk/TableMatrix/

%changelog
* Fri May 04 2007 Dag Wieers <dag@wieers.com> - 1.23-1
- Initial package. (using DAR)
