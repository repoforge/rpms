%bcond_with tests
%define rversion 4.2-0.8

Name:           bashdb
Summary:        BASH debugger, the BASH symbolic debugger
Version:        4.2_0.8
Release:        1%{?dist}
License:        GPLv2+
Group:          Development/Debuggers
Url:            http://bashdb.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{rversion}.tar.bz2
Buildroot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bash >= 4.1
BuildRequires:  python-pygments
Requires(post): /sbin/install-info
Requires(preun): /sbin/install-info
Requires:       bash >= 4.1
BuildArch:      noarch
Obsoletes:      emacs-bashdb, emacs-bashdb-el

%description
The Bash Debugger Project is a source-code debugger for bash,
which follows the gdb command syntax. 
The purpose of the BASH debugger is to check
what is going on “inside” a bash script, while it executes:
    * Start a script, specifying conditions that might affect its behavior.
    * Stop a script at certain conditions (break points).
    * Examine the state of a script.
    * Experiment, by changing variable values on the fly.
The 4.0 series is a complete rewrite of the previous series.
Bashdb can be used with ddd: ddd --debugger %{_bindir}/%{name} <script-name>.

%prep
%setup -q -n %{name}-%{rversion}

%build
%configure
make

%install
rm -rf %{buildroot}
make install INSTALL="install -p" DESTDIR=%{buildroot}
rm -f "%{buildroot}%{_infodir}/dir"

%if %{with tests}
%check
make check
%endif

%post
/sbin/install-info %{_infodir}/%{name}.info.gz %{_infodir}/dir || :

%postun
if [ "$1" = 0 ] && [ -f %{_infodir}/%{name}.info.gz ] ; then
   /sbin/install-info --delete %{_infodir}/%{name}.info.gz %{_infodir}/dir || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc doc/*.html AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_infodir}/%{name}.info*

%changelog
* Fri Oct 21 2011  <rocky@gnu.org> - 
- Initial build.
