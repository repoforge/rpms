# $Id$
# Authority: dag

# ExcludeDist: el4

%define real_name XML-Parser

Summary: XML-Parser Perl module
Name: perl-XML-Parser
Version: 2.34
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Parser/

Source: http://www.cpan.org/modules/by-module/XML/XML-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl >= 0:5.004, expat-devel
Requires: perl >= 0:5.004

%description
XML-Parser Perl module.

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
%{_libdir}/perl5/vendor_perl/*/*/XML/
%{_libdir}/perl5/vendor_perl/*/*/auto/XML/

%changelog
* Fri Nov 12 2004 Dag Wieers <dag@wieers.com> - 2.34-1
- Workaround directory-conflicts bug in up2date. (RHbz #106123)

* Sat Dec 20 2003 Dag Wieers <dag@wieers.com> - 2.34-0
- Initial package. (using DAR) 
