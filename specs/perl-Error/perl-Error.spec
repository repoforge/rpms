# $Id: perl-Convert-UUlib.spec 125 2004-03-16 22:05:34Z dag $
# Authority: matthias

%define real_name Error

Summary: %{real_name} module for perl
Name: perl-Error
Version: 0.15
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/%{real_name}/
Source: http://search.cpan.org/CPAN/authors/id/U/UA/UARUN/%{real_name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl >= 0:5.8.0
BuildRequires: perl >= 0:5.8.0
BuildArch: noarch

%description
%{summary}.


%prep
%setup -n %{real_name}-%{version}


%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL \
	PREFIX="%{buildroot}%{_prefix}" \
	INSTALLDIRS="vendor"
%{__make} %{?_smp_mflags} \
	OPTIMIZE="%{optflags}"


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
%doc Changes COPYING* MANIFEST README doc/*
%{_libdir}/perl5/vendor_perl/*/*
%{_mandir}/man?/*


%changelog
* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 0.15-1
- Initial RPM release.

