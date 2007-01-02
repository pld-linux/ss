Summary:	Console Screen Saver
Name:		ss
Version:	0.1
Release:	0.1
License:	RPL Rebane Public License (beerware)
Group:		Applications/System
Source0:	http://rebane.alkohol.ee/ss.c.txt
# Source0-md5:	ae57612c041d96b0edb4bfabf13017eb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux Console Screen Saver by Rebane.

%clean
rm -rf $RPM_BUILD_ROOT

%prep
%setup -qcT
cp %{SOURCE0} ss.c

%build
%{__cc} ss.c -o ss

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install ss $RPM_BUILD_ROOT%{_sbindir}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ss
