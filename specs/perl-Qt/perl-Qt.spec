# $Id$
# Authority: dag
# Upstream: Ashley Winters <awinters$users,sourceforge,net>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name PerlQt

Summary: Perl module for creating PerlQt applications
Name: perl-Qt
Version: 1.06
Release: 1
License: GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/PerlQt/

Source: http://www.cpan.org/modules/by-module/Qt/PerlQt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-PerlQt is a Perl module for creating PerlQt applications.

This package contains the following Perl modules:

    QTabBar
    QTabDialog
    QTableView
    QTimer
    QToolTip
    QWMatrix
    QWidget
    QWindow
    Qt

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
find contrib/ examples/ tutorial/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING CREDITS Changes INSTALL MANIFEST README README.PERLQT README.QT TODO contrib/ examples/ tutorial/
%doc %{_mandir}/man3/*.3pm*
%{perl_vendorarch}/Qt.pm
%{perl_vendorarch}/auto/Qt/

%changelog
* Thu Oct 11 2007 Dag Wieers <dag@wieers.com> - 1.06-1
- Initial package. (using DAR)
