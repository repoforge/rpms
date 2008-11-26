# $Id$
# Authority: dries
# Upstream: Steve McInerney <spm$stedee,id,au>

Summary: Web server log analysis program
Name: awffull
Version: 3.10.1
Release: 1
License: GPL
Group: Applications/Internet
URL: http://www.stedee.id.au/awffull

Source: http://www.stedee.id.au/files/awffull-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: zlib-devel, libpng-devel, db4-devel, gd-devel, pcre-devel

%description
AWFFull is a Web server log analysis program, forked from Webalizer. It
adds a number of new features and improvements, such as extended frontpage
history, resizable graphs, and a few more pie charts.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING INSTALL README TODO
%doc %{_mandir}/man1/awffull.1*
%doc %{_mandir}/man5/awffull.conf.5*
%{_bindir}/awffull

%changelog
* Wed Nov 26 2008 Dries Verachtert <dries@ulyssis.org> - 3.10.1-1
- Updated to release 3.10.1.

* Thu Nov 20 2008 Dries Verachtert <dries@ulyssis.org> - 3.9.1-1
- Updated to release 3.9.1.

* Tue Nov 20 2007 Dries Verachtert <dries@ulyssis.org> - 3.8.2-1
- Updated to release 3.8.2.

* Tue May 08 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.4-1
- Updated to release 3.7.4.

* Tue Jan 23 2007 Dries Verachtert <dries@ulyssis.org> - 3.7.2-1
- Updated to release 3.7.2.

* Sun Nov 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.7.1-1
- Updated to release 3.7.1.

* Sun Jun 04 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.3-1
- Updated to release 3.4.3.

* Sun Mar 26 2006 Dries Verachtert <dries@ulyssis.org> - 3.4.1-1
- Updated to release 3.4.1.

* Sun Feb 12 2006 Dries Verachtert <dries@ulyssis.org> - 3.3.1-1
- Updated to release 3.3.1.

* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 3.02-1
- Updated to release 3.02.

* Tue Dec 13 2005 Dries Verachtert <dries@ulyssis.org> - 3.01-1
- Initial package.
