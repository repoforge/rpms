# Authority: dag

%define rname Net-SMTP

Summary: Net-SMTP Perl module.
Name: perl-Net-SMTP
Version: 4.1.2
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Net-SMTP/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/D/DT/DTOWN/Net-SMTP-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503

%description
Net-SMTP Perl module.

%prep
%setup -n %{rname}-%{version} 

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README TODO
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Thu Mar 04 2004 Dag Wieers <dag@wieers.com> - 4.1.2-0
- Initial package. (using DAR)
