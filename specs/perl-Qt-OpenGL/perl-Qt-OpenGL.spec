# $Id$
# Authority: dag
# Upstream: Ashley Winters <awinters$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Qt-OpenGL

Summary: Perl module named Qt-OpenGL
Name: perl-Qt-OpenGL
Version: 0.02
Release: 1%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Qt-OpenGL/

Source: http://www.cpan.org/modules/by-module/Qt/Qt-OpenGL-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl
BuildRequires: perl(Qt) >= 2.104

%description
perl-Qt-OpenGL is a Perl module.

This package contains the following Perl module:

    Qt::OpenGL

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

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHANGES INSTALL MANIFEST README README.LICENSE examples/
%doc %{_mandir}/man3/Qt::OpenGL.3pm*
%dir %{perl_vendorarch}/Qt/
%{perl_vendorarch}/Qt/OpenGL.pm
%dir %{perl_vendorarch}/auto/Qt/
%{perl_vendorarch}/auto/Qt/OpenGL/

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 0.02-1
- Initial package. (using DAR)
