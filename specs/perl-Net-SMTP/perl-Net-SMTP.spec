# $Id$
# Authority: dag

### EL6 ships with perl-Net-SMTP-SSL-1.01-4.el6
%{?el6:# Tag: rfx}

%define real_name Net-SMTP

Summary: Net-SMTP Perl module
Name: perl-Net-SMTP
Version: 4.1.2
Release: 0.2%{?dist}
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMTP/

Source: http://www.cpan.org/modules/by-module/Net/Net-SMTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-SMTP Perl module.

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
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man3/Net:SMTP.3pm*
%{_libdir}/perl5/vendor_perl/Net/SMTP.pm
%{_libdir}/perl5/vendor_perl/Net/SMTP/

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 4.1.2-0
- Initial package. (using DAR)
