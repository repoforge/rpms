# $Id$

# Authority: dries
# Upstream: Burak Gürsoy <burak$cpan,org>

%define real_name MP3-M3U-Parser
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: MP3 playlist parser
Name: perl-MP3-M3U-Parser
Version: 2.1
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MP3-M3U-Parser/

Source: http://search.cpan.org/CPAN/authors/id/B/BU/BURAK/MP3-M3U-Parser-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Parses M3U mp3 playlists and if wanted, exports the parsed data to 
formats like xml and html.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod
%{__rm} -f %{buildroot}%{perl_vendorarch}/auto/*/*/*/.packlist

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MP3/M3U/Parser.pm

%changelog
* Wed Oct 20 2004 Dries Verachtert <dries@ulyssis.org> - 2.1-1
- Update to release 2.1.

* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 2.0-1
- Initial package.
