# $Id$
# Authority: dag

%define real_name Net-SMTP

Summary: Net-SMTP Perl module
Name: perl-Net-SMTP
Version: 4.1.2
Release: 0.2
License: distributable
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
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 4.1.2-0.2
- Rebuild for Fedora Core 5.

* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 4.1.2-0
- Initial package. (using DAR)
