# Authority: atrpms
%define rname XML-Simple

Summary: XML-Simple - Easy API to read/write XML (esp config files)
Name: perl-XML-Simple
Version: 2.08
Release: 0
License: distributable
Group: Applications/CPAN
URL: http://search.cpan.org/dist/XML-Simple/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://www.cpan.org/authors/id/G/GR/GRANTM/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildArch: noarch
BuildRequires: perl >= 0:5.00503, perl(XML::Parser)
Requires: perl >= 0:5.00503

%description
XML::Simple - Easy API to read/write XML (esp config files).

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
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Mon Jul 14 2003 Dag Wieers <dag@wieers.com> - 2.08-0
- Updated to release 2.08.

* Mon Mar 24 2003 Dag Wieers <dag@wieers.com> - 2.03-0
- Initial package. (using DAR)
