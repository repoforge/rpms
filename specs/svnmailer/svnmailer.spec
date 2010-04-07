# $Id$
# Authority: dries
# Upstream: Andre Malo <nd$perlig,de>

%define python_sitelib %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib()')

Summary: Notification script which can be used as subversion hook
Name: svnmailer
Version: 1.0.8
Release: 2%{?dist}
License: Apache License 2.0
Group: Development/Tools
URL: http://opensource.perlig.de/svnmailer/

Source: http://storage.perlig.de/svnmailer/svnmailer-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: python >= 2.3, subversion, python-devel
Requires: python >= 2.3

%description
The svnmailer is a tool that is usually called by a subversion hook to
submit commit notifications in various ways (at the moment: mail via SMTP
or a pipe to a sendmail like program, news via NNTP, or CIA live tracker
notification via XML-RPC). It is derived from the original mailer.py
distributed with subversion, but should be much more consistent, more
extensible, and have many more features.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build

%install
%{__rm} -rf %{buildroot}
python setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CREDITS LICENSE NOTICE README docs/
%{_bindir}/svn-mailer
%{python_sitelib}/svnmailer

%changelog
* Thu Jun 28 2007 Dag Wieers <dag@wieers.com> - 1.0.8-2
- Changed BuildArch to noarch. (Leo Eraly)
- Added --prefix to setup phase. (Leo Eraly)
- Added NOTICE and docs to %%doc.

* Fri Apr 21 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.8-1
- Updated to release 1.0.8.

* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1.2
- Rebuild for Fedora Core 5.

* Wed Mar 01 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.7-1
- Updated to release 1.0.7.

* Mon Feb 06 2006 Dries Verachtert <dries@ulyssis.org> - 1.0.6-1
- Updated to release 1.0.6.

* Mon Aug 29 2005 Dries Verachtert <dries@ulyssis.org> - 1.0.5-1
- Initial package.
