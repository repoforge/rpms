# $Id$
# Authority: dag

%define real_name Convert-TNEF

Summary: Convert-TNEF module for perl
Name: perl-Convert-TNEF
Version: 0.17
Release: 2
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Convert-TNEF/

Source: http://www.cpan.org/modules/by-module/Convert/Convert-TNEF-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 0:5.00503
Requires: perl >= 0:5.00503, perl-MIME-tools

%description
Convert-TNEF module for perl

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
%{__rm} -rf %{buildroot}%{_libdir}/perl5/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux-thread-multi/ \
                %{buildroot}%{_libdir}/perl5/vendor_perl/*/*-linux/

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man?/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
