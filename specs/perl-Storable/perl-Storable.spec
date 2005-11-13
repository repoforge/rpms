# $Id: perl-Convert-UUlib.spec 125 2004-03-16 22:05:34Z dag $
# Authority: matthias

# ExclusiveDist: rh6 el2 rh7

%define real_name Storable

Summary: %{real_name} module for perl
Name: perl-Storable
Version: 2.15
Release: 1
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/%{real_name}/

Source: http://search.cpan.org/CPAN/authors/id/A/AM/AMS/Storable-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: perl >= 0:5.8.0
BuildRequires: perl >= 0:5.8.0

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
find %{buildroot}%{_libdir} -name "*.so" -exec chmod u+w {} \;


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc MANIFEST README
%{_libdir}/perl5/vendor_perl/*/*
# No man pages...
#{_mandir}/man?/*


%changelog
* Sun Nov 13 2005 Dries Verachtert <dries@ulyssis.org> - 2.15-1
- Updated to release 2.15.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 2.11-1
- Initial RPM release.

