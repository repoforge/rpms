# $Id: perl-Convert-UUlib.spec 125 2004-03-16 22:05:34Z dag $
# Authority: matthias

%define real_name Cache-Cache

Summary: Cache-Cache module for perl
Name: perl-Cache-Cache
Version: 1.02
Release: 3
License: GPL or Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Cache-Cache/
Source: http://www.cpan.org/modules/by-module/Cache/Cache-Cache-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: perl >= 0:5.8.0
Requires: perl(Error), perl(Storable), perl(IPC::ShareLite)
BuildRequires: perl >= 0:5.8.0
BuildArch: noarch

%description
The Cache modules are designed to assist a developer in persisting data for a
specified period of time.  Often these modules are used in web applications to
store data locally to save repeated and redundant expensive calls to remote
machines or databases.  People have also been known to use Cache::Cache for
its straightforward interface in sharing data between runs of an application
or invocations of a CGI-style script or simply as an easy to use abstraction
of the filesystem or shared memory.


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
%doc COPYING* MANIFEST README
%{_libdir}/perl5/vendor_perl/*/*
%{_mandir}/man?/*


%changelog
* Wed May 26 2004 Matthias Saou <http://freshrpms.net/> 1.02-3
- Rebuilt for Fedora Core 2.

* Fri Apr  2 2004 Matthias Saou <http://freshrpms.net/> 1.02-2
- Change the explicit package deps to perl package style ones to fix the
  perl-Storable obsoletes problem.

* Fri Mar 19 2004 Matthias Saou <http://freshrpms.net/> 1.02-1
- Initial RPM release.

