# Authority: dag

%define rname Jcode

Summary: Jcode (Japanese Charset Handler) module for perl.
Name: perl-Jcode
Version: 0.83
Release: 0
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Jcode/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANKOGAI/%{rname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/root-%{name}-%{version}
Prefix: %{_prefix}

BuildRequires: perl >= 0:5.8.0
Requires: perl >= 0:5.8.0

%description
Jcode (Japanese Charset Handler) module for perl.

%prep
%setup -n %{rname}-%{version}

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
%{__rm} -f %{buildroot}%{_libdir}/perl5/*/i386-linux-thread-multi/perllocal.pod

%clean 
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST README
%doc %{_mandir}/man?/*
%{_libdir}/perl5/

%changelog
* Wed Jan 21 2004 Dag Wieers <dag@wieers.com> - 0.83-0
- Initial package. (using DAR)
