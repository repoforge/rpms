# $Id$
# Authority: dag
# Upstream: Eryq <eryq$zeegee,com>
# Upstream: David F. Skoll <dfs$roaringpenguin,com>
# Upstream: Dave O'Neill <dmo$roaringpenguin,com>

# Tag: test

%{?dtag: %{expand: %%define %dtag 1}}

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MIME-tools

Summary: Tools to manipulate MIME messages
Name: perl-MIME-tools
Version: 5.426
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MIME-tools/

Source: http://www.cpan.org/modules/by-module/MIME/MIME-tools-%{version}.tar.gz
Patch: http://www.roaringpenguin.com/mimedefang/mime-tools-patch.txt
Patch1: MIME-Tools.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl >= 2:5.8.0
BuildRequires: perl-MailTools
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Temp) >= 0.17
BuildRequires: perl(IO::Stringy) >= 1.211
BuildRequires: perl(Test::More)
Requires: perl >= 2:5.8.0
Requires: perl-MailTools >= 1.15
Requires: perl(File::Temp) >= 0.17
Requires: perl(IO::Stringy) >= 1.211
%{?rh7:BuildRequires: perl(MIME::Base64) >= 2.04}
%{?el2:BuildRequires: perl-MIME-Base64 >= 2.04}

%description
MIME-tools - modules for parsing (and creating!) MIME entities Modules in this
toolkit : Abstract message holder (file, scalar, etc.), OO interface for
decoding MIME messages, an extracted and decoded MIME entity, Mail::Field
subclasses for parsing fields, a parsed MIME header (Mail::Header subclass),
parser and tool for building your own MIME parser, and utilities.

%prep
%setup -n %{real_name}-%{version}
#patch -p1
#patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}
#{__make} test

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

### Clean up docs
find examples/ -type f -exec %{__chmod} a-x {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING ChangeLog INSTALLING MANIFEST MANIFEST.SKIP META.yml README README-OR-DIE README.system examples/
%doc %{_mandir}/man3/MIME::*.3pm*
%{perl_vendorlib}/MIME/

%changelog
* Wed May 14 2008 Dag Wieers <dag@wieers.com> - 5.426-1
- Updated to release 5.426.

* Mon Nov 19 2007 Dag Wieers <dag@wieers.com> - 5.425-2
- Added dependency to perl(File::Temp) >= 0.17. (Christof Damian)

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 5.425-1
- Updated to release 5.425.

* Tue Aug 07 2007 Dag Wieers <dag@wieers.com> - 5.420-2
- Disabled auto-requires for examples/.

* Mon Apr 17 2006 Dag Wieers <dag@wieers.com> - 5.420-1
- Updated to release 5.420.

* Fri Jan 13 2006 Dag Wieers <dag@wieers.com> - 5.419-1
- Updated to release 5.419.

* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org> - 5.418-2
- Rebuild.

* Sat Nov  5 2005 Dries Verachtert <dries@ulyssis.org> - 5.418-1
- Updated to release 5.418.

* Thu Mar 10 2005 Dag Wieers <dag@wieers.com> - 5.417-1
- Updated to release 5.417.

* Mon Dec 20 2004 Dag Wieers <dag@wieers.com> - 5.415-1
- Updated to release 5.415.

* Sun Jan 26 2003 Dag Wieers <dag@wieers.com>
- Initial package. (using DAR)
