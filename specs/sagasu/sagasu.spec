# $Id$
# Authority: dag
# Upstream: Pierre Sarrazin <sarrazip$sympatico,ca>

Summary: Tool to find strings in a set of files
Name: sagasu
Version: 2.0.8
Release: 1.2%{?dist}
License: GPL
Group: Applications/Text
URL: http://sarrazip.com/dev/sagasu.html

Source: http://www3.sympatico.ca/sarrazip/dev/sagasu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libgnomeui-devel >= 2.0.0
BuildRequires: gcc-c++
Requires: libgnomeui >= 2.0.0

%description
GNOME tool to find words in a set of files.
The user specifies the search directory and the set of files
to be searched.  Double-clicking on a search result launches a
user command that can for example load the file in an editor
at the appropriate line.  The search can optionally ignore
CVS directories.

%prep
%setup

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/sagasu/
%{_bindir}/*
%{_datadir}/sagasu/
%{_datadir}/sounds/sagasu/
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%exclude %{_docdir}

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.8-1.2
- Rebuild for Fedora Core 5.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.8-1
- Updated to release 2.0.8.

* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.

* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 2.0.5-0
- Updated to release 2.0.5.

* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Updated to release 2.0.4.

* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Updated to release 2.0.3.

* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.

* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
