# $Id$
# Authority: yury
# Upstream: Dave Hall <dave$etianen,com>

%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%{?el5:%define _with_python24 1}

%define real_name django-reversion

Name: python-%{real_name}
Version: 1.5
Release: 1%{?dist}
Summary: Version control extension for the Django web framework
Group: Development/Languages
License: BSD
URL: http://github.com/etianen/django-reversion

Source0: http://github.com/downloads/etianen/%{real_name}/%{real_name}-%{version}.tar.gz
Patch0: django-reversion-1.5-python2.4.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch

BuildRequires: python-devel >= 2.4

Requires: python-django >= 1.3

%description
Reversion is an extension to the Django web framework that provides
comprehensive version control facilities. Reversion can be easily added to your
existing Django project with a minimum of code changes.

%prep
%setup -n %{real_name}-%{version}

%if 0%{?_with_python24}
%patch0 -p1
%{__rm} src/reversion/test*.py
%endif

%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

# Language files; not under /usr/share, need to be handled manually
(cd $RPM_BUILD_ROOT && find . -name 'django*.mo') | %{__sed} -e 's|^.||' | %{__sed} -e \
  's:\(.*/locale/\)\([^/_]\+\)\(.*\.mo$\):%lang(\2) \1\2\3:' \
  >> %{name}.lang

find $RPM_BUILD_ROOT -name "*.po" | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root, -)
%doc PKG-INFO LICENSE README.markdown
%dir %{python_sitelib}/reversion
%{!?_with_python24:%{python_sitelib}/*.egg-info}
%{python_sitelib}/reversion/*.py*
%{python_sitelib}/reversion/management/
%{python_sitelib}/reversion/migrations/
%{python_sitelib}/reversion/templates/

%changelog
* Thu Sep 08 2011 Yury V. Zaytsev <yury@shurup.com> - 1.5-1
- Updated to release 1.5.

* Sun Nov 14 2010 Luca Botti <lucabotti@fedoraproject.org> 1.3.2-2
- Fixed locale handling

* Fri Nov 11 2010 Luca Botti <lucabotti@fedoraproject.org> 1.3.2-1
- Update to 1.3.2

* Tue Sep 29 2009 Luca Botti <lucabotti@fedoraproject.org> 1.1.2-2
- Fixed Spec File

* Fri Aug 21 2009 Luca Botti <lucabotti@fedoraproject.org> 1.1.2-1
- Update to 1.1.2 upstream release

* Fri Jul 17 2009 Tim Niemueller <timn@fedoraproject.org> 1.1.1
- Initial RPM release
