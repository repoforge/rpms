# $Id: perl-Archive-Tar.spec 120 2004-03-15 17:26:20Z dag $

# Authority: dag

%define real_name Net-SNPP

Summary: Perl Simple Network Pager Protocol Client
Name: perl-Net-SNPP
Version: 1.16
Release: 1
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SNPP/

Source: http://search.cpan.org/CPAN/authors/id/T/TO/TOBEYA/Net-SNPP-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root


BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Simple Network Pager Protocol Client.

%prep
%setup -n %{real_name}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/
%{__rm} -f %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/auto/*{,/*}/.packlist

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 1.16-1
- Initial package. (using DAR)
