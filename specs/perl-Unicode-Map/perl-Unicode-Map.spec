# $Id$
# Authority: dag

%define real_name Unicode-Map

Summary: Unicode-Map (Maps charsets from and to UTF16 unicode) module for perl
Name: perl-Unicode-Map
Version: 0.112
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-Map/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-Map-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Unicode-Map (Maps charsets from and to UTF16 unicode) module for perl.

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
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/*/*

%changelog
* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.112-0
- Initial package. (using DAR)
