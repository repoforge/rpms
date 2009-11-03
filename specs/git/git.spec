# $Id$
# Authority: dag

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%{?dtag: %{expand: %%define %dtag 1}}

Summary: Git core and tools
Name: git
Version: 1.5.2.1
Release: 2%{?dist}
License: GPL
Group: Development/Tools
URL: http://git.or.cz/

Source: http://kernel.org/pub/software/scm/git/git-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, openssl-devel, curl-devel >= 7.9
BuildRequires: perl(ExtUtils::MakeMaker)
Requires: sh-utils, diffutils, rsync, rcs, mktemp >= 1.5

Obsoletes: git-arch <= %{version}-%{release}
Provides: git-arch = %{version}-%{release}
Obsoletes: git-cvs <= %{version}-%{release}
Provides: git-cvs = %{version}-%{release}
Obsoletes: git-email <= %{version}-%{release}
Provides: git-email = %{version}-%{release}
Obsoletes: git-svn <= %{version}-%{release}
Provides: git-svn = %{version}-%{release}

%description
GIT comes in two layers. The bottom layer is merely an extremely fast
and flexible filesystem-based database designed to store directory trees
with regard to their history. The top layer is a SCM-like tool which
enables human beings to work with the database in a manner to a degree
similar to other SCM tools (like CVS, BitKeeper or Monotone).

%package gui
Summary: Graphical frontend to git
Group: Development/Tools

Requires: %{name} = %{version}-%{release}
Requires: tk >= 8.4

%description gui
Graphical frontend to git.

%package -n perl-Git
Summary: Perl module that implements Git bindings
Group: Applications/CPAN

Requires: %{name} = %{version}-%{release}

%description -n perl-Git
Git is a Perl module that implements Git bindings.

%prep
%setup

%build
%{__make} %{?_smp_mflags} all CFLAGS="%{optflags}" prefix="%{_prefix}" WITH_OWN_SUBPROCESS_PY="YesPlease"

### Perl preparation
cd perl
%{__perl} Makefile.PL PREFIX="%{buildroot}%{_prefix}" INSTALLDIRS="vendor"
#%{__make} %{?_smp_mflags}
cd -

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}" CFLAGS="%{optflags}" prefix="%{_prefix}" mandir="%{_mandir}" INSTALLDIRS="vendor"

### Perl installation
#%makeinstall -C perl INSTALLDIRS="vendor"

### Clean up buildroot
find %{buildroot}%{_bindir} -type f -exec %{__perl} -pi -e 's|^%{buildroot}||' {} \;
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc COPYING Documentation/*.txt README
#%{!?_without_asciidoc:%doc %{_mandir}/man1/*.1*}
#%{!?_without_asciidoc:%doc %{_mandir}/man7/*.7*}
%{_bindir}/git*
%exclude %{_bindir}/git-citool
%exclude %{_bindir}/git-gui
%{_datadir}/git-core/

%files gui
%defattr(-, root, root, 0755)
%{_bindir}/git-citool
%{_bindir}/git-gui
%{_datadir}/git-gui/

%files -n perl-Git
%defattr(-, root, root, 0755)
%doc %{_mandir}/man3/Git.3pm*
%{perl_vendorlib}/Git.pm

%changelog
* Sun Nov 25 2007 Dag Wieers <dag@wieers.com> - 1.5.2.1-2
- Fix group tag.

* Mon Jun 11 2007 Dag Wieers <dag@wieers.com> - 1.5.2.1-1
- Update to release 1.5.2.1.

* Sat Jun 09 2007 Dag Wieers <dag@wieers.com> - 1.5.0.6-1
- Update to release 1.5.0.6.

* Wed Feb 14 2007 Dries Verachtert <dries@ulyssis.org> - 0.99.4-3
- Fix location of templates (Dave Miller).
- Option '--unsafe' added to call to asciidoc.
- Fix asciidoc problem with '^'.

* Sun Aug 14 2005 Dries Verachtert <dries@ulyssis.org> - 0.99.4-1
- Update to release 0.99.4.

* Wed Aug 10 2005 Dag Wieers <dag@wieers.com> - 0.99.1-1
- Small cleanup.
- Added documentation using asciidoc.

* Wed Jul 07 2005 Chris Wright <chris@osdl.org> - 0.99-1
- Initial git spec file.
